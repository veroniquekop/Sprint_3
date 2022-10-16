from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/chromedriver")

driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(*TestLocators.Search_button_main_locator).click()

driver.get("https://stellarburgers.nomoreparties.site/login")
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
email = driver.find_elements(*TestLocators.Input_email_locator)[0]
email.send_keys("user169@yandex.ru")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))

# Найди поле "Пароль" и заполни его
password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
driver.find_element(*TestLocators.Log_in_locator).click()


driver.quit()