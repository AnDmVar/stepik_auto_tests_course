from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(10)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#browser.execute_script("window.scrollBy(0, 100);")
time.sleep(10)
button.click()
browser.quit()
