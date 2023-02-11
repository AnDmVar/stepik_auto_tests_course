from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

#    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
#    input1.send_keys("First name")
#    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
#    input2.send_keys("Last name")
#    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
#    input3.send_keys("Email")


    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first")
    input4.send_keys("Phone")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second")
    input5.send_keys("Address")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1').text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt
    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
