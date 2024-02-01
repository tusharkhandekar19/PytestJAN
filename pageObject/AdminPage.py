from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Select

class AdminPageClass:
    Text_ClickAdmin_XPATH = (By.XPATH, "//a[@class='oxd-main-menu-item active']")
    Text_Username_XPATH = (By.XPATH, "//input[@class='oxd-input oxd-input--focus']")
    Text_UserRole_XPATH = (By.XPATH, "//div[@class='oxd-select-text oxd-select-text--focus']//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")
    Text_EmpName_XPATH = (By.XPATH, "//input[@placeholder='Type for hints...']")
    Text_Select_XPATH = (By.XPATH, "//div[@class='oxd-select-text oxd-select-text--focus']//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")

    def __init__(self, driver):
        self.driver = driver

    def Select_Admin(self, admin):
        self.driver.find_element(*AdminPageClass.Text_ClickAdmin_XPATH).click()

    def UserName(self, username):
        self.driver.find_element(*AdminPageClass.Text_Username_XPATH).send_keys(username)

    def UserRole(self, userrole):
        self.driver.find_element(*AdminPageClass.Text_UserRole_XPATH)
        ele = self.driver.find_element(*AdminPageClass.Text_UserRole_XPATH)
        dropdown = Select(ele)
        dropdown.Select_by_Index(1)

    def EmpName(self, empname):
        self.driver.find_element(*AdminPageClass.Text_EmpName_XPATH).send_keys(empname)

    def Select(self, select):
        self.driver.find_element(*AdminPageClass.Text_Select_XPATH)
        elm = self.driver.find_element(*AdminPageClass.Text_Select_XPATH)
        dropdown = Select(elm)
        dropdown.Select_by_Index(1)
