import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import userLogin_Class


class Test_Login:

    def test_userLogin_001(self, setup):
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(3)
        self.ur = userLogin_Class(self.driver)

        self.ur.Enter_UserName("Admin")
        time.sleep(3)
        self.ur.Enter_Password("admin123")

        self.ur.ClickOn_Login("Login")
        time.sleep(3)

        # try:
        #     self.driver.find_element(By.XPATH, "//div[@class='oxd-topbar-header']")
        #     print("Login Successful")
        #     self.driver.quit()
        #     return "Login pass"
        # except:
        #     print("Login UnSuccessful")
        #     return "Loin Fail"
