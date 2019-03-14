from selenium import webdriver
import time
import string
import random

driverChrome=webdriver.Chrome("C:\\Python\\insider\\chromedriver.exe")

def mailGenerator(chars=string.ascii_lowercase):
    mail= ''.join(random.choice(chars) for _ in range(random.randint(5,15)))
    mailList=["@gmail.com","@hotmail.com","@yahoo.com","@yandex.com"]
    mail=mail+random.choice(mailList)
    return mail
def nameGenerator(chars=string.ascii_lowercase):
    name= ''.join(random.choice(chars) for _ in range(random.randint(5,15)))
    return name
def userGenerator(driver=driverChrome):
    driver.get("https://www.modanisa.com")
    driver.find_element_by_id("headerRegisterUrl").click()
    driver.find_element_by_xpath("//form[@id='register-form']/div/label[2]/input").click()
    driver.find_element_by_id("term").click()
    driver.find_element_by_id("register-form").find_element_by_id("email").send_keys(mailGenerator())
    driver.find_element_by_id("name").send_keys(nameGenerator())
    driver.find_element_by_id("surname").send_keys(nameGenerator())
    driver.find_element_by_xpath("//form[@id='register-form']/div[7]/input").click()
def randomVisitPages(driver=driverChrome):
    driver.get("https://www.modanisa.com")
    driver.find_element_by_id("header-menu").find_element_by_xpath("//ul[@class='nav']/li["+str(random.randint(3,8))+"]").find_element_by_tag_name("a").click()
    driver.find_element_by_xpath("//ul[@id='productsList']/li["+str(random.randint(1,30))+"]").click()
    time.sleep(1)
    listElement=driver.find_elements_by_id("size-box-container")
    if len(listElement)>0:
        driver.find_element_by_xpath("//div[@id='size-box-container']/select/option[2]").click()
        
    driver.find_element_by_id("add-to-favorite-btn").click()
    driver.find_element_by_id("addtobasket").find_element_by_tag_name("a").click()
    if driver.find_element_by_id("size-guide-container")!=None:
        driver.find_element_by_id("size-guide-container").find_element_by_tag_name("a").click()
        driver.find_element_by_id("addtobasket").find_element_by_tag_name("a").click()
    
userGenerator()
randomVisitPages()

