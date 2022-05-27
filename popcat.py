from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import time
path="D:/chromedriver_win32/chromedriver.exe"


driver=webdriver.Chrome(path)
driver.get("https://popcat.click/")

# blow=driver.find.el

# action=ActionChains(driver)
# action.click()
c=driver.find_element_by_xpath('//*[@id="app"]/div')
while True:
    c.click()