from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.goibibo.com/")
driver.find_element(By.CSS_SELECTOR,".sc-gsFSXq.bGTcbn").click()
# from_input= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='From']/..//p[text()='Enter city or airport']")))
# from_input.click()
# time.sleep(10)

from_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='From']/..//p[text()='Enter city or airport']"))
)
from_input.send_keys("del")

from_values =driver.find_element(By.XPATH,"//li[@role='presentation']")
for departure in from_values:
    depar = departure.text
    if depar == "New Delhi, India":
        departure.click()