from POMDemo.Locators.locators import Locators
from POMDemo.GenericMethods.Methods import Methods

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcomeLink    = Locators.welcome_link_id
        self.logOut = Locators.logout_link_linkText

    def click_welcome(self):
        Methods.clickElement(self, self.welcomeLink)

    def click_logout(self):
        Methods.clickElement(self, self.logOut)