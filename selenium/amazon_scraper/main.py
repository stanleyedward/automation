import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

with open("data.json", "w") as f:
    json.dump([],f)

def write_json (new_data, filename = "data.json"):
    with open(filename, 'r+') as file:
        #first we load existing data into a dict.
        file_data = json.load(file)
        #join new_data with file_data inside emp_details
        file_data.append(new_data)
        #sets file's current postion at offset.
        file.seek(0)
        #convert back into json
        json.dump(file_data, file, indent =4)

# os.environ['PATH'] += r"/home/stanley/Desktop/geckodriver-v0.33.0-linux64"
browser = webdriver.Firefox()
browser.implicitly_wait(5)
# browser.get("https://www.amazon.in/")
browser.get("https://www.amazon.in/s?k=razer+gaming+mouse&ref=nav_bb_sb")

# search_element = browser.find_element(By.ID,"twotabsearchtextbox")
# search_element.click()
# search_element.send_keys('razer gaming mouse')
# submit_search_element = browser.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
# submit_search_element.click()

# single_mouse_element= browser.find_element(By.CSS_SELECTOR,
#                                          'img[alt="Razer DeathAdder Essential Wired Gaming Mouse I Single-Color Green Lighting I 6400DPI Optical Sensor- Black - RZ01-0385010..."]')
is_next_disabled = False
while not is_next_disabled:
    # single_mouse_element.click()
    elem_list = browser.find_element(By.XPATH,
                                    '//span[@data-component-type="s-search-results"]')
    # items = elem_list.find_element(By.CLASS_NAME,
    #                                "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
    # print(len(items))
    items = elem_list.find_elements(By.XPATH,
                                '//div[@data-component-type="s-search-result"]')
    # print(len(items))
    for item in items:
        title = item.find_element(By.TAG_NAME, 'h2').text
        price= "no price found"
        img = 'no image found'
        url = item.find_element(By.CSS_SELECTOR,'a[class="a-link-normal s-no-outline"]').get_attribute('href')
        try:
            price = item.find_element(By.CSS_SELECTOR, 'span[class="a-price"]').text.replace("\n",".")
        except:
            pass
        try:
            img = item.find_element(By.CSS_SELECTOR,
                                    'img[class="s-image"]').get_attribute("src")
        except:
            pass

        print(f'Title: {title}')
        print(f'Price: {price}')
        # print(f'Image: {img}')
        # print(f'URL: {url}\n')

        write_json({
            "title": title,
            "price": price,
            "Link": url
        })
    
    try:
        next_button_element = browser.find_element(By.CSS_SELECTOR,
                                               'a[class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
        next_button_element.click()
    except Exception as e:
        print(e,"error here")
        is_next_disabled = True
