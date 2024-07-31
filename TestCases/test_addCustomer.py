import pytest
from PageOject.LoginPage import Login
from TestData.data import CustomerData, DataJson
from PageOject.CustomerPage import AddCustomer
from TestData.data import URL


@pytest.mark.sanity
@pytest.mark.run(order=2)
@pytest.mark.usefixtures("setup")
class TestAddCustomer:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)
        self.add = AddCustomer(self.driver)

    def test_add_new_customer(self, setup):
        self.driver = setup

        customer = CustomerData.data
        user = DataJson.data[4]

        self.login.verify_email_field(Login.email, user['email'])
        self.login.verify_password(Login.password, user['password'])
        self.login.verify_login_btn()

        self.add.verify_main_customer_link(AddCustomer.main_customers_link)
        self.add.verify_sub_customer_link(AddCustomer.sub_customers_link)

        self.add.verify_page_header(AddCustomer.customer_page_header)
        self.add.verify_customer_url(URL.customer_url)
        self.add.verify_add_new_customer_btn(AddCustomer.add_new_customer_btn)

        self.add.verify_add_cust_email_field(AddCustomer.add_email, customer['email'])
        self.add.verify_add_cust_firstname_field(AddCustomer.add_firstname, customer['firstname'])
        self.add.verify_add_cust_lastname_field(AddCustomer.add_lastname, customer['lastname'])
        self.add.verify_add_cust_company_field(AddCustomer.add_company_name, customer['company'])
        self.add.verify_add_cust_role_field(AddCustomer.add_cust_roles)
        self.add.verify_add_cust_save_btn(AddCustomer.save_btn)

        try:
            error_message = self.add.verify_add_cust_already_reg_notif()
            success_message = self.add.verify_add_cust_success_notif()

            if AddCustomer.registered_notification == error_message:
                print(error_message)
            else:
                print(success_message)
        except Exception as e:
            print(f"An error occurred: {e}")








