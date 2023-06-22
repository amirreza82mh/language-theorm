from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def cfg_to_cnf(grammar_str):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Open the website
    driver.get("https://cyberzhg.github.io/toolbox/cfg2cnf")

    try:
        # Find the input box and enter your text
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "input_grammar"))
        )
        input_box.send_keys(grammar_str)

        time.sleep(10)
        # Find the button and click it
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button_convert"))
        )
        button.click()

        time.sleep(5)
        # Wait for the output box to appear and retrieve the output
        output_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "output_grammar"))
        )
        output = output_box.text

        return output

    finally:
        # Close the browser
        driver.quit()
