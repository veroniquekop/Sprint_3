from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestConstructor:
    def test_constructor_to_sauce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(*TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.Sauce_tab_locator).click()
        driver.implicitly_wait(10)
        driver.find_element(*TestLocators.Example_sauce_locator).click()
        driver.get('https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73')
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa73'
