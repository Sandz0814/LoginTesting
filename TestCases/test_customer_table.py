import time
import pytest
from PageOject.CustomerPage import AddCustomer
from PageOject.LoginPage import Login
from TestData.data import Creds


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self, setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.add = AddCustomer(self.driver)

        self.login.verify_logo(Login.logo)
        self.login.verify_email_field(Login.email, Creds.email)
        self.login.verify_password(Login.password, Creds.password)
        self.login.verify_login_btn()
        self.login.verify_logot_text_assertion(Login.logout)

        self.add.verify_main_customer_link(AddCustomer.main_customers_link)
        self.add.verify_sub_customer_link(AddCustomer.sub_customers_link)

        self.add.email_column_data(AddCustomer.table)
        time.sleep(10)






