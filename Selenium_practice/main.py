import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def setup_driver():
    """
    Setup WebDriver

    :return: driver
    """
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.get("https://www.selenium.dev/selenium/web/index.html")
    return driver


def navigate_to_webform(driver):
    """
    Open the main page and navigate to webform
    :param driver: WebDriver
    :return: None
    """
    element_webform = driver.find_element(By.LINK_TEXT, "web-form.html")
    element_webform.click()
    time.sleep(0.5)


def fill_text_input(driver, text: str):
    """
    Fill the text input file
    :param driver: WebDriver
    :param text: Text to be input
    :return: None
    """
    element_textinput = driver.find_element(By.ID, "my-text-id")
    element_textinput.send_keys(text)
    time.sleep(0.5)


def select_number_from_dropdown(driver, number_int: int, number_str: str):
    """
    Select a number from dropdown menu using two methods.
    :param driver: WebDriver
    :param number_int: Number to choose for Select method: int
    :param number_str: Number to choose for send_keys method: str
    :return: None
    """
    Select(driver.find_element(By.NAME, "my-select")).select_by_value(value=str(number_int))
    time.sleep(0.25)
    element_select = driver.find_element(By.NAME, "my-select")
    element_select.send_keys(number_str)
    time.sleep(0.5)


def select_color(driver, color: str):
    """
    Select a color.
    :param driver: WebDriver
    :param color: Hex value needed so it works better
    :return: None
    """
    element_color = driver.find_element(By.NAME, "my-colors")
    element_color.send_keys(color)
    time.sleep(0.5)


def pick_date(driver, date: str):
    """
    Pick a date from the calendar.
    :param driver: WebDriver
    :param date: string, format: month/day/year
    :return: None
    """
    element_date_pick = driver.find_element(By.NAME, "my-date")
    element_date_pick.click()
    element_date_pick.send_keys(date)
    element_date_pick.send_keys(Keys.RETURN)
    element_date_pick.send_keys(Keys.TAB)
    time.sleep(0.5)


def move_slider(driver, direction: str, steps: int):
    """
    Move the slider by mouse click and drag or arrow keys.
    :param driver: WebDriver
    :param direction: Choose "L" or "R" for left or right
    :param steps: Number of key strokes or steps
    :return: None
    """
    element_slider = driver.find_element(By.NAME, "my-range")
    move = webdriver.ActionChains(driver)
    move.click_and_hold(element_slider).move_by_offset(80, 0).release().perform()
    time.sleep(0.5)
    if direction.upper() == "R":
        for step in range(steps):
            element_slider.send_keys(Keys.ARROW_RIGHT)
            time.sleep(0.25)
    elif direction.upper() == "L":
        for step in range(steps):
            element_slider.send_keys(Keys.ARROW_LEFT)
            time.sleep(0.25)


def upload_file(driver, file):
    """
    Upload file via File Input
    :param driver: WebDriver
    :param file: name of the file
    :return: None
    """
    file_path = os.path.abspath(file)
    element_file_upload = driver.find_element(By.NAME, "my-file")
    element_file_upload.send_keys(file_path)
    time.sleep(0.5)


def submit_form(driver):
    """
    Submit button click
    :param driver: WebDriver
    :return: None
    """
    element_submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
    element_submit.click()
    time.sleep(0.5)


def select_radio_and_checkbox(driver):
    """
    Select "default radio" and uncheck the Checked box
    :param driver: WebDriver
    :return: None
    """
    element_checked_radio = driver.find_element(By.ID, "my-check-1")
    element_checked_radio.click()
    time.sleep(0.5)
    element_default_radio = driver.find_element(By.ID, "my-radio-2")
    element_default_radio.click()
    time.sleep(0.5)


def select_city_from_datalist(driver, city: str):
    """
    Select a city from the list dropdown
    :param driver: WebDriver
    :param city: Choose a city from the list
    :return: None
    """
    element_dropdown = driver.find_element(By.NAME, "my-datalist")
    element_dropdown.send_keys(city)
    element_dropdown.send_keys(Keys.TAB)
    time.sleep(0.5)


def return_to_index_link(driver):
    """
    Return to index. Click.
    :param driver: WebDriver
    :return: None
    """
    element_return_link = driver.find_element(By.LINK_TEXT, "Return to index")
    element_return_link.click()
    time.sleep(0.5)


def go_back(driver):
    """
    Go to the previous page
    :param driver: WebDriver
    :return: None
    """
    driver.back()
    time.sleep(0.5)


def main():
    driver = setup_driver()

    try:
        navigate_to_webform(driver)
        fill_text_input(driver, "Some text goes here and there!")
        select_number_from_dropdown(driver, number_int=2, number_str="one")
        select_city_from_datalist(driver, "Seattle")
        upload_file(driver, "File_to_upload.txt")
        select_radio_and_checkbox(driver)
        select_color(driver, "#FFFF00")
        pick_date(driver, "01/25/1999")
        move_slider(driver, "L", 5)
        submit_form(driver)
        go_back(driver)
        return_to_index_link(driver)

    except Exception as e:
        print(f"An error has occurred: {e}")
    finally:
        time.sleep(1)
        driver.quit()


if __name__ == '__main__':
    main()
