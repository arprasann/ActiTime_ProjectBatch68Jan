import pytest
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import time
import inspect
import logging

@pytest.mark.usefixtures("loginandlogoutsetup")
class BaseClass:

    def verify_element_presence(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((idtype, text)))

    def verify_element_clickable(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((idtype, text)))

    def verify_element_Visible(self, idtype, text):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((idtype, text)))

    def click_on_element(self,idtype,value):
        self.driver.find_element(idtype,value).click()

    def enter_text(self,idtype,value,text1):
        self.driver.find_element(idtype,value).send_keys(text1)

    def scroll_Bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def waitforsometime(self):
        time.sleep(2)

    def waitTenSecond(self):
        time.sleep(10)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger