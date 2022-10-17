from selenium import webdriver
from tests.locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/chromedriver")

driver.get("https://stellarburgers.nomoreparties.site/register")

# Найди поле имя и заполни его
name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")


# Найди поле "Email" и заполни его
email = driver.find_elements(*TestLocators.Input_email_locator)[1]
email.send_keys("user161@yandex.ru")

# Найди поле "Пароль" и заполни его
email = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")

# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(*TestLocators.Log_in_locator).click()

driver.get("https://stellarburgers.nomoreparties.site/login")
assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user161@yandex.ru")

# Найди поле "Пароль" и заполни его
password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")

driver.find_element(*TestLocators.Log_in_locator).click()
WebDriverWait(driver, 10)
driver.quit()
