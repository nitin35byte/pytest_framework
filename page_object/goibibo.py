from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait


class FlightBooking:
    login_signup_cancel_css = ".sc-gsFSXq.bGTcbn"
    from_xpath = "(//p[@class='sc-12foipm-6 erPfRs'])[1]"
    list_from_element_xpath = "//li[@role='presentation']"
    to_xpath = "//span[text()='To']/..//p[text()='Enter city or airport']"
    cancel_css = ".sc-jlwm9r-1.ewETUe"

    def __init__(self, driver):
        self.driver = driver

    def cancel_login(self):
        try:
            cancel_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_signup_cancel_css))
            )
            cancel_btn.click()
        except Exception as e:
            print(f"An error occurred while cancelling login: {e}")

    def cancel_btn(self):
        try:
            cancel_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.cancel_css))
            )
            cancel_btn.click()
        except Exception as e:
            print(f"An error occurred while clicking cancel button: {e}")

    def From(self):
        try:
            from_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.from_xpath))
            )
            ##from_input.click()
            from_input.send_keys("del")

            from_values = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.list_from_element_xpath))
            )
            for departure in from_values:
                depar = departure.text
                if depar == "New Delhi, India":
                    departure.click()
                    break
        except Exception as e:
            print(f"An error occurred in From method: {e}")

    def To(self):
        try:
            to_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.to_xpath))
            )
            ##to_input.click()
            to_input.send_keys("pune")

            to_values = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.list_from_element_xpath))
            )
            for arrival in to_values:
                arr = arrival.text
                if arr == "Pune, India":
                    arrival.click()
                    break
        except Exception as e:
            print(f"An error occurred in To method: {e}")
