import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from main import password, username


@pytest.fixture()
def setUp():
    global product,driver
    username = input("Enter Username")
    password = input("Enter password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_searchproducts(setUp):
    driver.get("https://www.facebook.com/")
    time.sleep(5)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("login").click()
    time.sleep(10)
    driver.close()