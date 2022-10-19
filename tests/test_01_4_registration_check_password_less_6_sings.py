from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestRegistration:
   def test_registration_via_password_less_6_signs(self, driver):
      driver.get("https://stellarburgers.nomoreparties.site/register")
      name = driver.find_element(*TestLocators.Input_name_locator).send_keys("Вероника")
      WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Вероника']")))
      email = driver.find_elements(*TestLocators.Input_email_locator)[1]
      email.send_keys("user159@yandex.ru")
      WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user159@yandex.ru']")))
      password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir19")
      WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir19']")))
      driver.find_element(*TestLocators.Log_in_locator).click()

      password = str(password)
      if len(password) < 6:
         return 'Некорректный пароль'
      else:
         return 'Правильный пароль'




