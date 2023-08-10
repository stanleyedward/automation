#this file will include class with instance methods which will be repsobislb eto intereact with websites
#after we have some results to apply filters
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFilteration:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    
    def apply_star_rating(self):
        star_filteration_box = self.driver.find_element(
            By.ID,
            'filter_group_class_:r96:'
        )
        star_child_elements = star_filteration_box.find_elements(
            By.CSS_SELECTOR,
            '*'
        )
        print(len(star_child_elements))