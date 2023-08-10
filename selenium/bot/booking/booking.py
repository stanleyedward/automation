#responsible to call methods
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Firefox): #the class will inherit the webdriver.firefox module, 
    #we want this as we want the self obj to have the option of both using wedirver.chrome and the user defined methods that we'll design for booking
    def __init__(self,driver_path=r'/home/stanley/Desktop/geckodriver-v0.33.0-linux64', teardown = False):  #constructor, ie called imidiately as soon as we create an obj/ instantiate it
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH']+= self.driver_path
        super(Booking, self).__init__() # instantiate the webdriver class ie create an obj of webdriver module
        self.implicitly_wait(15) #every element with prefix find_element is gonna wait maximum 15 seconds
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tab):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)   #as the website we use wont change

    def change_currency(self, currency=None): 
        currency_element=self.find_element(
            By.CSS_SELECTOR,
              'button[data-testid="header-currency-picker-trigger"]'
              )
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR,'div[class="b1e6dd8416 aacd9d0b0a e3d479393e"]')
        selected_currency_element.click()

        # IF THE USD CURRENCY WAS IN A SUBSTRING
        # selected_currency_element = self.find_element(
        #     By.CSS_SELECTOR,
        #     f'a[data-model-header-async-url-param*="selected_currency={currency}"]'
        # )
        # selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field=self.find_element(
            By.ID,':rc:' #id is the best filtering u can get!
        )
        search_field.clear() #clears existing text
        search_field.send_keys(place_to_go)

        #from tutorial to select first result
        # first_result = self.find_element(
        #     By.CSS_SELECTOR,
        #     'li[data-i="0"]'
        # )
        # first_result.click()


        #we commented coz we were having issues v
        # first_manual_result = self.find_element(By.CSS_SELECTOR,'div[class="d8eab2cf7f"]')
        # first_manual_result.click()


        WebDriverWait(self,30).until(  #explicit_waiting 
        EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "f9afbb0024"), #element filteration
        'New York')#the expected text
        )
        first_manual_result = self.find_element(By.CSS_SELECTOR,'div[class="d8eab2cf7f"]')
        first_manual_result.click()

    def select_date(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def adults_count(self, count):
        selection_element = self.find_element(
            By.CSS_SELECTOR,
            'span[data-testid="searchbox-form-button-icon"]'
        )
        selection_element.click()

        while True:
            
            decrease_adults_element = self.find_element(
            By.CSS_SELECTOR,
            'path[d="M20.25 12.75H3.75a.75.75 0 0 1 0-1.5h16.5a.75.75 0 0 1 0 1.5z"]'
            )
            decrease_adults_element.click()
            #if the value of adults reaches 1 then we should get out of the while loop
            adults_value_element = self.find_element(
                By.ID,
                'id="group_adults"'
            )
            adults_value = adults_value_element.get_attribute('value') ##should give adults count 

            if int(adults_value)==1:
                break
        
        increase_adults_element = self.find_element(
            By.CSS_SELECTOR,
            'path[d="M20.25 11.25h-7.5v-7.5a.75.75 0 0 0-1.5 0v7.5h-7.5a.75.75 0 0 0 0 1.5h7.5v7.5a.75.75 0 0 0 1.5 0v-7.5h7.5a.75.75 0 0 0 0-1.5z"]'
        )
        for i in range(count-1):
            increase_adults_element.click()

        