
from selenium import webdriver
from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/chromedriver")

driver.get("https://stellarburgers.nomoreparties.site/register")

# Найди поле имя и заполни его
name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")

WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Вероника']")))

# Найди поле "Email" и заполни его
email = driver.find_elements(*TestLocators.Input_email_locator)[1]
email.send_keys("user159@yandex.ru")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user159@yandex.ru']")))
def registration(email):
   email= str(email)
   driver.test.get_new_email('user159@yandex.ru')
   assert driver.get_new_email == 'user159@yandex.ru'
# Найди поле "Пароль" и заполни его
password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir41941@")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir41941@']")))

# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(*TestLocators.Log_in_locator).click()

WebDriverWait(driver, 10)
driver.quit()
