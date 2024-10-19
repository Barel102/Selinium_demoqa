import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def website_main_page(driver):
    driver.get("https://demoqa.com/")
    element_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='card-body']/h5[text()='Elements']"))
    )
    element_button.click()


def test_text_box(driver):
    website_main_page(driver)

    text_box_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space() = 'Text Box']"))
    )
    text_box_button.click()

    full_name_text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='userName']"))
    )
    full_name_text_box.send_keys(FULL_NAME)

    email_text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='userEmail']"))
    )
    email_text_box.send_keys(EMAIL)

    current_address_text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@id='currentAddress']"))
    )
    current_address_text_box.send_keys(CURRENT_ADDRESS)

    permanent_address_text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@id='permanentAddress']"))
    )
    permanent_address_text_box.send_keys(PERMANENT_ADDRESS)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))
    )
    submit_button.click()

    assert FULL_NAME in WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@id='name']"))
    ).text, "Name not found in the output!"

    assert EMAIL in WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@id='email']"))
    ).text, "Email not found in the output!"

    assert CURRENT_ADDRESS in WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@id='currentAddress']"))
    ).text, "Current address not found in the output!"

    assert PERMANENT_ADDRESS in WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[@id='permanentAddress']"))
    ).text, "Permanent address not found in the output!"


def test_check_box(driver):
    website_main_page(driver)

    # Click the "Check Box" button
    check_box_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space() = 'Check Box']"))
    )
    check_box_button.click()

    # Expand all the checkboxes
    expand_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Expand all']"))
    )
    expand_all_button.click()

    # Get the list of all checkboxes
    boxs_list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@class='rct-checkbox']"))
    )

    for checkbox in boxs_list:
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", checkbox)

            WebDriverWait(driver, 10).until(EC.visibility_of(checkbox))

            checkbox_input = checkbox.find_element(By.XPATH, ".//input")

            if checkbox_input.is_selected():
                print("Checkbox is already selected.")
            else:
                checkbox.click()

                assert checkbox_input.is_selected(), "Checkbox was not selected!"

        except Exception as e:
            print(f"Could not interact with checkbox: {e}")

    WebDriverWait(driver, 10)


def test_radio_button(driver):
    website_main_page(driver)

    radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Radio Button']"))
    )
    radio_button.click()

    yes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']"))
    )
    yes_button.click()

    yes_radio_selected = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='yesRadio']"))
    )
    assert yes_radio_selected.is_selected(), "Yes radio button was not selected!"

    impressive_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='impressiveRadio']"))
    )
    impressive_button.click()

    impressive_radio_selected = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='impressiveRadio']"))
    )
    assert impressive_radio_selected.is_selected(
    ), "Impressive radio button was not selected!"
