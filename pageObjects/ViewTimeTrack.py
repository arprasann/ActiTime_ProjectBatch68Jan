from selenium import webdriver

from selenium.webdriver.common.by import By
from utilites.base import BaseClass

class ViewTimeTrack(BaseClass):
    viewTimeTRack = (By.XPATH,"//a[text()='View Time-Track']")
    viewTimeTRackDropdown = (By.XPATH,"//input[@id='ext-comp-1001']/following::img")
    dropdownValue = (By.XPATH,"(//span[@class='userName'])[3]")


    def __init__(self,driver):
        self.driver  = driver


    def clickOnViewTimeTrack(self):
        return self.driver.find_element(*ViewTimeTrack.viewTimeTRack).click()


    def clickOnViewTimeTRackDropdown(self):
        return self.driver.find_element(*ViewTimeTrack.viewTimeTRackDropdown).click()

    def selectViewTrackdropdownValue(self):
        return  self.driver.find_element(*ViewTimeTrack.dropdownValue).click()