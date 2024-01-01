from selenium.webdriver.common.by import By

from utilites.base import BaseClass

class Reports(BaseClass):

    report = (By.XPATH,"//div[text()='REPORTS']")

    newReport = (By.XPATH,"//span[text()='New Report']")

    configurereport = (By.XPATH,"//input[@id='configureReportParametersButton']")



    exportcsvreport = (By.XPATH, "(//span[text()='Generate HTML Repor'])[2]")

    def __init__(self,driver):
        self.driver = driver

    def clcikonreport(self):
        self.verify_element_clickable(By.XPATH,"//div[text()='REPORTS']")
        return self.driver.find_element(*Reports.report).click()

    def clcikoncreatereport(self):
        self.verify_element_clickable(By.XPATH,"//span[text()='New Report']")
        return self.driver.find_element(*Reports.newReport).click()

    def clcikonconfigurereport(self):
        self.verify_element_clickable(By.XPATH,"//input[@id='configureReportParametersButton']")
        return self.driver.find_element(*Reports.configurereport).click()

    def clcikonexportcsvreport(self):
        self.verify_element_clickable(By.XPATH, "(//span[text()='Generate HTML Report'])[2]")
        return self.driver.find_element(*Reports.exportcsvreport).click()