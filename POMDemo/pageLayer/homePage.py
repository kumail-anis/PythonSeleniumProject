from POMDemo.POM.homePOM import HomePage

class homePage():

    def logOut(driver):

        homepage = HomePage(driver)
        homepage.click_welcome()
        print("clicked on welcome btn")
        homepage.click_logout()