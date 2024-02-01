
from selenium import webdriver
from selenium.webdriver.common.by import By


class userLogin_Class:
    Text_Username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Enter_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_LoginButton_XPATH = (By.XPATH, "//button[@type='submit']")
    # View_Dashboard_XPATH = (By.XPATH, "//div[@class='oxd-topbar-header']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_UserName(self, username):
        self.driver.find_element(*userLogin_Class.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*userLogin_Class.Enter_Password_XPATH).send_keys(password)

    def ClickOn_Login(self, login):
        self.driver.find_element(*userLogin_Class.Click_LoginButton_XPATH).click()



