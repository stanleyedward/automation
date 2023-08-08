import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #highlight 'Keys' and pres f12:)

os.environ['PATH'] += r"/home/stanley/Desktop/geckodriver-v0.33.0-linux64"
driver = webdriver.Firefox()

# driver.get('http://127.0.0.1:5500/test_websites/webiste2/add_2.html')
driver.get('http://127.0.0.1:5500/test_websites/website1/add.html')
driver.implicitly_wait(10)
try:
    enter_button = driver.find_element(By.ID,'enterBtn')
    print('enter button found!')
    enter_button.click()
except:
    print('No element with that "enterBtn" ID. skipping...')

element_1 = driver.find_element(By.ID,'num1')
element_2 = driver.find_element(By.ID,'num2')
# calculate_button = driver.find_element(By.ID,'addBtn')   #also works!!
btn = driver.find_element(By.CSS_SELECTOR,'button[id="addBtn"]')
element_1.send_keys(Keys.NUMPAD3, Keys.NUMPAD8)
element_2.send_keys(15)
# calculate_button.click() #works
btn.click()



#we can also send keys directly and not just the text like shift alt ctrl, etc..