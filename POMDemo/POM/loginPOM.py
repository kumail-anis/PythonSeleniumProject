from POMDemo.Locators.locators import Locators
from POMDemo.GenericMethods.Methods import Methods

class LoginPage():


    def __init__(self, driver):
        self.driver = driver

        self.userName = Locators.username_textbox_id
        self.password = Locators.password_textbox_id
        self.loginBtn = Locators.login_button_id

    def enter_username(self, username):
        Methods.sendKey(self, self.userName, username)
        
    def enter_password(self, password):
        Methods.sendKey(self, self.password, password)

    def click_login(self):
        Methods.clickElement(self, self.loginBtn)