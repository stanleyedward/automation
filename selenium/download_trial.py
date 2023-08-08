import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] +=  r"/home/stanley/Desktop/geckodriver-v0.33.0-linux64" #r makes it as a role string
driver = webdriver.Firefox()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(20)#('time in seconds')wait time to allow website to load (runs asap after loading tho)
#implicity wait stops all driver functions together
# my_element = driver.find_element(By.ID,'downloadButton')#searches id in HTML
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()

# progress_element = driver.find_element(By.CLASS_NAME, "progress-label")
# print(f"{progress_element.text=='Completed!'}") #doesNT work

WebDriverWait(driver,30).until(  #explicit_waiting 
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), #element filteration
        'Complete!'#the expected text
    )
)
print('Complete!')

#sending keys and clicking buttons is for login and registering accounts
