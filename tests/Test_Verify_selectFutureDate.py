from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout
from utilites.base import BaseClass
from pageObjects.FutureCalendarDate import FutureCalendarDate

class TestFutureCalendarDate(BaseClass):
    def test_verify_viewtrack(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()
        self.waitforsometime()

        futuredate = FutureCalendarDate(self.driver)
        futuredate.click_on_calendar()
        self.waitforsometime()
        futuredate.click_on_calendar_menubar()
        self.waitforsometime()
        futuredate.click_on_select_Year()
        self.waitforsometime()
        futuredate.click_on_Ok_Button()
        self.waitforsometime()
        futuredate.selct_date()
        self.waitforsometime()
        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()