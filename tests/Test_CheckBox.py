from pageObjects.CheckBox import CheckBox
from utilites.base import BaseClass

class TestCheckbox(BaseClass):

    def test_validate_Checkbox_selectedORNot(self):
        checkbox = CheckBox(self.driver)
        self.waitforsometime()
        checkbox.clickoncheckbox()
        self.waitTenSecond()
