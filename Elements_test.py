import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Constants for test data
FULL_NAME = "Barel"
EMAIL = "barel@gmail.com"
CURRENT_ADDRESS = "Jerusalem"
PERMANENT_ADDRESS = "Israel"


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_text_box(driver):
    driver.get("https://demoqa.com/")
    print("Navigated to the demo site.")

    element_button = driver.find_element(By.XPATH, "//div[@class='card-body']/h5[text()='Elements']")
    element_button.click()

    text_box_button = driver.find_element(By.XPATH, "//span[normalize-space() = 'Text Box']")
    text_box_button.click()

    full_name_text_box = driver.find_element(By.XPATH, "//input[@id='userName']")
    full_name_text_box.send_keys(FULL_NAME)

    email_text_box = driver.find_element(By.XPATH, "//input[@id='userEmail']")
    email_text_box.send_keys(EMAIL)

    current_address_text_box = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    current_address_text_box.send_keys(CURRENT_ADDRESS)

    permanent_address_text_box = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
    permanent_address_text_box.send_keys(PERMANENT_ADDRESS)

    submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    submit_button.click()


    assert FULL_NAME in driver.find_element(
        By.XPATH, "//p[@id='name']").text, "Name not found in the output!"
    assert EMAIL in driver.find_element(
        By.XPATH, "//p[@id='email']").text, "Email not found in the output!"
    assert CURRENT_ADDRESS in driver.find_element(
        By.XPATH, "//p[@id='currentAddress']").text, "Current address not found in the output!"
    assert PERMANENT_ADDRESS in driver.find_element(
        By.XPATH, "//p[@id='permanentAddress']").text, "Permanent address not found in the output!"

