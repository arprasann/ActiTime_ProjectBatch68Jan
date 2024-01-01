
from utilites.base import BaseClass

from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout

from  pageObjects.ViewTimeTrack import ViewTimeTrack


class Test_Verify_ViewTrackValue(BaseClass):

    def test_verify_viewtrack(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()
        self.waitforsometime()

        views = ViewTimeTrack(self.driver)
        views.clickOnViewTimeTrack()
        views.clickOnViewTimeTRackDropdown()
        self.waitforsometime()
        views.selectViewTrackdropdownValue()



        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()

