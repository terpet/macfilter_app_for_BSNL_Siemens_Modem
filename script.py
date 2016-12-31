from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.set_window_size(1,1)
def changeMACmode():
    try:
        print("Opening Siemens DSL Router Configuration page.")
        driver.get('http://admin:admin@192.168.1.1')
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    except:
        driver.get('http://admin:admin@192.168.1.1')   
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    print("Page Opened !")
    
    wireless=driver.find_element_by_link_text("Wireless")
    print("Clicking 'Wireless' Link !")
    wireless.click()
    
    
    macfilter=driver.find_element_by_link_text("MAC Filter")
    print("Clicking 'MAC Filter' Link !")
    macfilter.click()
    
    
    driver.switch_to.default_content()
    
    driver.switch_to.frame(driver.find_element_by_name("basefrm_0"))
    
    
    
    print("Enter Your Choice \n1.Disable MAC Filter\n2.Enable MAC Filter")
    choice=int(raw_input())
    if choice==2:
        check2=driver.execute_script(" with ( document.forms[0] ) { if(wlFltMacMode[2].checked == true) return 1; else return 0;}")
        if check2==1:
            print('MAC Filter Already Enabled!')
        else:    
            driver.execute_script(" with ( document.forms[0] ) { wlFltMacMode[0].checked = false;wlFltMacMode[2].checked = true; modeClick();}")
            print('MAC Filter has been Enabled!')
    elif choice==1:
        check1=driver.execute_script(" with ( document.forms[0] ) { if(wlFltMacMode[0].checked == true) return 1; else return 0;}")
        if check1==1:
            print('MAC Already Disabled!')
        else:
            driver.execute_script(" with ( document.forms[0] ) { wlFltMacMode[2].checked = false;wlFltMacMode[0].checked = true; modeClick();}")
            print('MAC Filter has been Disabled!')
    
    driver.close()
   
    
def addMAC(macaddress):
    try:
        print("Opening Siemens DSL Router Configuration page.")
        driver.get('http://admin:admin@192.168.1.1')
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    except:
        driver.get('http://admin:admin@192.168.1.1')   
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    print("Page Opened !")
    
    wireless=driver.find_element_by_link_text("Wireless")
    print("Clicking 'Wireless' Link !")
    wireless.click()
    
    
    macfilter=driver.find_element_by_link_text("MAC Filter")
    print("Clicking 'MAC Filter' Link !")
    macfilter.click()
    
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("basefrm_0"))
    
    addButton = driver.find_element_by_xpath("//input[@value='Add']") 
    addButton.click()    
    
    addrField=driver.find_element_by_xpath("//input[@name='wlFltMacAddr']") 
    addrField.click()
    addrField.send_keys(macaddress)
    
    
    submitButton=driver.find_element_by_xpath("//input[@value='Save/Apply']") 
    submitButton.click()
    print("The MAC Address Has Been Added")    
    driver.close()
    
    
def removeMAC(macaddress):
    try:
        print("Opening Siemens DSL Router Configuration page.")
        driver.get('http://admin:admin@192.168.1.1')
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    except:
        driver.get('http://admin:admin@192.168.1.1')   
        driver.switch_to.frame(driver.find_element_by_name("menufrm"))
    print("Page Opened !")
    
    wireless=driver.find_element_by_link_text("Wireless")
    print("Clicking 'Wireless' Link !")
    wireless.click()
    
    
    macfilter=driver.find_element_by_link_text("MAC Filter")
    print("Clicking 'MAC Filter' Link !")
    macfilter.click()
    
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name("basefrm_0"))
 
    try:
        addr=driver.find_element_by_xpath("//input[@value='"+macaddress+"']") 
        addr.click()
    except:
        print("The MAC Address does not exist")
         
    submitButton=driver.find_element_by_xpath("//input[@value='Remove']") 
        
    submitButton.click()
    print("The MAC Address has been removed")    
    time.sleep(1)    
    driver.close()
    
def main():
    print("Siemens DSL Router MAC Filter App")
    print("Developed & Maintained By : Tarpit Sahu")
    print("1.Change MAC Filter Mode")
    print("2.Add a MAC Address to Block List")
    print("3.Remove a MAC Address from Block List")
    print("\nEnter Your Choice : ")
    ch=int(raw_input())
    
    if ch==1:
        changeMACmode()
    elif ch==2:
        print("Enter The MAC Address : ")
        string=raw_input()
        addMAC(string)
    elif ch==3:
        print("Enter The MAC Address : ")
        string=raw_input()
        removeMAC(string)
          
main()
