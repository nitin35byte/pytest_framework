import time

import pytest
from selenium import webdriver
from page_object.goibibo import FlightBooking
from utilities.custom_logger import LogGen
from utilities.readproperties import ReadConfig

class Testflight_booking():
    baseURL= ReadConfig.getApplicationURL()
    logger= LogGen.loggen(__name__)

    def test_book_flight(self,setup):
        self.logger.info("_________Test Execution Started_______________")
        self.driver=setup
        self.driver.get(self.baseURL)
        title=self.driver.title
        print(title)
        self.booking=FlightBooking(self.driver)
        self.booking.cancel_login()
        self.booking.From()
        self.booking.To()
        self.driver.save_screenshot(r"C:\Users\Admin\Desktop\Automation\pytest_framework\screen_shots\test_addCustomer_scr.png")
        self.logger.info("_____________Execution END___________________________")



