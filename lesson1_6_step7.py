from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    str = "Я памятник себе воздвиг нерукотворный К нему не зарастет народная тропа Вознесся выше он главою непокорной Александрийского столпа"
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(random.choice(str.split()))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
