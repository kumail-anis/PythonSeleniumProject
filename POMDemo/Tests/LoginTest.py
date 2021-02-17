from selenium import webdriver
import time, unittest, sys, os, socket, platform

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POMDemo.pageLayer.loginPage import loginPage
from POMDemo.pageLayer.homePage import homePage
from POMDemo.GenericMethods.driverSetup import setupClass

def test_login_valid():
      
    try:
        driver = setupClass.chromeSetup() 
        loginPage.login(driver)
        homePage.logOut(driver)
    except Exception as err:
        raise err
    finally:
        driver.close()


# to use Unittesting method
# class LoginTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("Driver Opening")
#         cls.driver = webdriver.Chrome(Locators.chromeDriver)
#         cls.driver.implicitly_wait(10)

#     def test_login_valid(self):
#         driver = self.driver
#         driver.get(Locators.website)

#         loginPage.login(driver)
#         homePage.logOut(driver)

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#         print("Test Completed")

if __name__ == '__main__':
    test_login_valid()