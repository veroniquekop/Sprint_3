from tests.locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestAuthorization:
    def test_authorization_the_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
        email = driver.find_elements(*TestLocators.Input_email_locator)[1]
        email.send_keys("user151@yandex.ru")
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user151@yandex.ru")
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir2469@")
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(driver, 10)
    def test_authorization_the_private_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_button = driver.find_elements(*TestLocators.Search_personal_button_main_locator)[0]
        personal_button.click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_authorization_in_the_system(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.Search_button_main_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = driver.find_elements(*TestLocators.Input_email_locator)[0]
        email.send_keys("user169@yandex.ru")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
        password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
        driver.find_element(*TestLocators.Log_in_locator).click()
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    def test_authorization_via_recovery_form(self, driver):
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
        driver.get("https://stellarburgers.nomoreparties.site/register")
    def test_logout_from_account(self, driver):
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
            driver.implicitly_wait(10)
            logout_button = driver.find_element(*TestLocators.Logout_button_locator).click()
            driver.get("https://stellarburgers.nomoreparties.site/login")
            assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"