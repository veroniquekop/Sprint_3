
from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestRegistation:
    def test_registration_by_name(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Вероника']")))
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user159@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user159@yandex.ru']")))
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        name = str(name)
        if len(name) > 1:
            return "Корректное имя"
        else:
            return "Поле пустое"


