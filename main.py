from selenium import webdriver as wb
import time
from secrets import *


class ChromeDriver:

    def __init__(self):
        self.driver = wb.Chrome(secret['driver_path'])



class Login(ChromeDriver):

    def  __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        

    def login_page(self):

        self.driver.get('https://to-do.microsoft.com/tasks/')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="actionButton"]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="i0116"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        self.driver.find_element_by_xpath('//*[@id="i0118"]').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        time.sleep(1)


if __name__ == "__main__":
    
    mylogin = Login(secret['username'], secret['password'])
    mylogin.login_page()
