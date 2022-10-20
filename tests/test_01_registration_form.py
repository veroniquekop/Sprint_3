from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestRegistation:
    def test_registration_check_name(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Вероника']")))
        password = driver.find_element(*TestLocators.Input_name_locator).get_attribute("value")
        name = str(name)
        assert len(name) > 1

        #ввод email
    def test_registration_check_email(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user158@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user158@yandex.ru']")))
        email = driver.find_element(*TestLocators.Input_email_locator).get_attribute("value")
        email = str(email)
        assert len(email)<256 or email.count('@') ==1


    def test_registration_check_password_less_6_signs(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user158@yandex.ru")
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir19")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir19']")))
        driver.find_element(*TestLocators.Input_password_locator).get_attribute("value")
        password = str(password)
        assert len(password) < 6, 'Некорректный пароль'
        driver.find_element(*TestLocators.Log_in_locator).click()
        WebDriverWait(driver, 10)

    def test_registration_check_password_more_6_signs(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user158@yandex.ru")
        driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        driver.find_element(*TestLocators.Input_password_locator).get_attribute("value")
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"









