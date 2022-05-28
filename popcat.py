from selenium import webdriver
path="D:/chromedriver_win32/chromedriver.exe"#放chromedriver的檔案路徑


driver=webdriver.Chrome(path)
driver.get("https://popcat.click/")


c=driver.find_element_by_xpath('//*[@id="app"]/div')
while True:
    c.click()
