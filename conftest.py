import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/chromedriver")
    yield driver
    driver.quit()
