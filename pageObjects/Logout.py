from selenium.webdriver.common.by import By
from utilites.base import BaseClass

class Logout(BaseClass):

    logout = (By.ID,"logoutLink")
    
    def __init__(self,driver):
        self.driver = driver


    def clickonlogoutbutton(self):
        self.verify_element_clickable(By.ID,"logoutLink")
        return self.driver.find_element(*Logout.logout).click()