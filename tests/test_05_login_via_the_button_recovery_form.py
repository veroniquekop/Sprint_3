from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestLogin:
    def test_login_via_button_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.Recover_password_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
        driver.find_element(*TestLocators.Recovery_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/reset-password")
        driver.find_element(*TestLocators.Login_button_locator).click()
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
        email = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
