from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestMove:
    def test_logo_moving(self, driver):
       driver.get("https://stellarburgers.nomoreparties.site/")
       personal_button = driver.find_elements(*TestLocators.Search_personal_button_main_locator)[0]
       personal_button.click()
       driver.get("https://stellarburgers.nomoreparties.site/login")
       email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
       password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
       driver.find_element(*TestLocators.Log_in_locator).click()
       personal_button = driver.find_element(*TestLocators.Search_personal_button_main_locator).click()
       logo = driver.find_element(*TestLocators.Logo_button_locator).click()
       driver.get("https://stellarburgers.nomoreparties.site/")
       assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
       WebDriverWait(driver, 15)


