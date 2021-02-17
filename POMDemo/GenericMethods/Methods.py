class Methods():

    def __init__(self, driver):
        self.driver = driver

    def clickElement(self, elementName):

        if "//" not in elementName:
            print("element is an ID")
            self.driver.find_element_by_id(elementName).click()
        else:
            print("element is an xpath")
            self.driver.find_element_by_xpath(elementName).click()

    def sendKey(self, elementName, elementText):

        if "//" not in elementName:
            self.driver.find_element_by_id(elementName).clear()
            self.driver.find_element_by_id(elementName).send_keys(elementText)
        else:
            self.driver.find_element_by_xpath(elementName).clear()
            self.driver.find_element_by_xpath(elementName).send_keys(elementText)
       
