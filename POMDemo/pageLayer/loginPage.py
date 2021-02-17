
from POMDemo.POM.loginPOM import LoginPage

class loginPage():

    def login(driver):
        login = LoginPage(driver)
        print("Logging in with Admin user")
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        print("Clicking Login page")