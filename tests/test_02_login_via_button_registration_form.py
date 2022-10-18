from tests.locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    def test_login_via_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user161@yandex.ru")
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user161@yandex.ru")
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 10)

