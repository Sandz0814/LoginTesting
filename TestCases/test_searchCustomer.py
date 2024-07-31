import time
import pytest
from PageOject.LoginPage import Login
from TestData.data import CustomerData, DataJson
from PageOject.CustomerPage import AddCustomer


@pytest.mark.sanity
@pytest.mark.run(order=3)
@pytest.mark.usefixtures("setup")
class TestSearchCustomer:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)
        self.add = AddCustomer(self.driver)

    def test_add_new_customer(self, setup):
        self.driver = setup

        customer = CustomerData.data
        user = DataJson.data[4]

        # Login Process
        self.login.verify_email_field(Login.email, user['email'])
        self.login.verify_password(Login.password, user['password'])
        self.login.verify_login_btn()

        # Clicking Customer main link and Customer sub-link
        self.add.verify_main_customer_link(AddCustomer.main_customers_link)
        self.add.verify_sub_customer_link(AddCustomer.sub_customers_link)

        # Type the email address to search
        self.add.verify_searched_input_field(AddCustomer.search_input_field, 'admin@yourStore.com')

        # Clicking Search button
        self.add.verify_search_customer_btn(AddCustomer.search_cust_btn)
        time.sleep(5)

        # Verifying the Search action
        search_details = self.add.verify_searched_customer_info(AddCustomer.searched_customer)
        assert 'admin@yourStore.com' in search_details
        time.sleep(10)
