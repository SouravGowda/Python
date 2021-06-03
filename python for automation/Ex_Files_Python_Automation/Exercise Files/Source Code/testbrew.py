import time

from selenium import webdriver



driver = webdriver.Chrome('chromedriver_linux64/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

#PRINT
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello sourav')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()


#TOTAL
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')

additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('20')

getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()




# time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# driver.quit()
