import socket, platform, os, sys
from selenium import webdriver
from POMDemo.Locators.locators import Locators

class setupClass():

    def chromeSetup():
        name = socket.gethostname()
        system = platform.system()

        if len(name) == 12 and system == 'Linux':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            driver = webdriver.Chrome(Locators.chromeDriver)
            driver.implicitly_wait(10)
        
        driver.get(Locators.website)
        return driver