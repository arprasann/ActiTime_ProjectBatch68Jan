from selenium import webdriver
from selenium.webdriver.common.by import By

class FutureCalendarDate:

    #Click on Calendar
    calendar = (By.ID,"ext-gen23")
    calendarMenuBar = (By.XPATH,"//button[text()='December 2023']")
    selectYear = (By.XPATH,"//a[text()='2026']")
    okButton = (By.XPATH,"//button[contains(text(),'OK')]")
    selectDate = (By.XPATH,"//span[text()='9']")

    def __init__(self,driver):
        self.driver = driver


    def click_on_calendar(self):
        return self.driver.find_element(*FutureCalendarDate.calendar).click()

    def click_on_calendar_menubar(self):
        return self.driver.find_element(*FutureCalendarDate.calendarMenuBar).click()

    def click_on_select_Year(self):
        return self.driver.find_element(*FutureCalendarDate.selectYear).click()

    def click_on_Ok_Button(self):
        return self.driver.find_element(*FutureCalendarDate.okButton).click()

    def selct_date(self):
        return self.driver.find_element(*FutureCalendarDate.selectDate).click()
