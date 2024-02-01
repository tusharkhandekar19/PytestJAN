# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pageObject.AdminPage import AdminPageClass
#
#
# class Test_Admin:
#
#     def test_Admin(self, setup):
#         self.driver = setup
#         self.driver.maximize_window()
#         time.sleep(3)
#
#         self.ad = AdminPageClass(self.driver)
#
#         self.ad.Select_Admin("Admin")
#
#         self.ad.UserName("Tushar@19")
#
#         self.ad.UserRole("")
#
#         self.ad.EmpName("Tushar")
#
#         self.ad.Select()
