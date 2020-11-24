from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
i = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_css_selector("#input_value").text
e = browser.find_element_by_css_selector("#answer")
e.send_keys(calc(int(x)))

b = browser.find_element_by_css_selector("button[type='submit']")
b.click()
