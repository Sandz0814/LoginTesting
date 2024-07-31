import time
from selenium.webdriver.common.by import By
from commands.script_min import Command
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer(Command):

    main_customers_link = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    sub_customers_link = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    customer_page_header = "//h1[normalize-space()='Customers']"
    add_new_customer_btn = "//a[normalize-space()='Add new']"

    add_email = "//input[@id='Email']"
    add_firstname = "//input[@id='FirstName']"
    add_lastname = "//input[@id='LastName']"
    add_dob = "//input[@id='DateOfBirth']"
    add_company_name = "//input[@id='Company']"
    add_cust_roles = "//select[@id='SelectedCustomerRoleIds']"
    select_option = "//option[@value='4']"
    save_btn = "//button[@name='save']"
    add_cust_success_notif = "//div[@class='alert alert-success alert-dismissable']"
    add_cust_already_registered = "//li[normalize-space()='Email is already registered']"

    registered_notification = "Email is already registered"
    success_notification = "The new customer has been added successfully."

    search_cust_btn = "//button[@id='search-customers']"
    searched_customer = "//td[normalize-space()='admin@yourStore.com']"
    search_input_field = "//input[@id='SearchEmail']"

    table = "//table[@id='customers-grid']/tbody/tr/td[2]"

    def verify_main_customer_link(self, selector):
        self.find_xpath(selector).click()

    def verify_sub_customer_link(self, selector):
        self.find_xpath(selector).click()

    def verify_page_header(self, selector):
        header = self.find_xpath(selector).text
        assert 'Customers' in header

    def verify_add_new_customer_btn(self, selector):
        self.find_xpath(selector).click()

    def verify_customer_url(self, url):
        assert url in self.driver.current_url

    def verify_add_cust_email_field(self, selector, email):
        self.find_xpath(selector).send_keys(email)

    def verify_add_cust_firstname_field(self, selector, firstname):
        self.find_xpath(selector).send_keys(firstname)

    def verify_add_cust_lastname_field(self, selector, lastname):
        self.find_xpath(selector).send_keys(lastname)

    def verify_add_cust_company_field(self, selector, company):
        self.find_xpath(selector).send_keys(company)

    def verify_add_cust_role_field(self, role):
        self.find_xpath("//span[@role='presentation']").click()
        cust_role = self.find_xpath(role)
        select = Select(cust_role)
        select.select_by_value("4")

    def verify_add_cust_save_btn(self, selector):
        self.find_xpath(selector).click()

    def verify_add_cust_success_notif(self):
        success_alert = self.find_xpath(self.add_cust_success_notif).text
        return success_alert

    def verify_add_cust_already_reg_notif(self):
        registered_alert = self.find_xpath(self.add_cust_already_registered).text
        return registered_alert

    def verify_search_customer_btn(self, selector):
        self.find_xpath(selector).click()

    def verify_searched_input_field(self, selector, email):
        self.find_xpath(selector).send_keys(email)

    def verify_searched_customer_info(self, selector):
        searched_info = self.find_xpath(selector).text
        return searched_info

    def email_column_data(self, selector):

        tar = "brenda_lindgren@nopCommerce.com"
        x = self.find_elements(selector)

        found = False  # Initialize a flag to track if the target word is found

        for i in x:
            y = i.text
            if y == tar:  # Check for exact match
                print(y)
                found = True  # Set the flag to True if the target word is found

        if not found:  # Check the flag after the loop
            print("not in the list")








