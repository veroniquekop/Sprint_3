from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait

class TestMove:
    def test_move_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(*TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
        email = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        driver.find_element(*TestLocators.Log_in_locator).click()
        personal_button = driver.find_element(*TestLocators.Search_personal_button_main_locator).click()
        driver.find_element(*TestLocators.Constructor_button_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 10)


