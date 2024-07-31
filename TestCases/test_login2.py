import pytest
from PageOject.LoginPage import Login
from TestData.data import DataJson, URL


# @pytest.mark.sanity
@pytest.mark.run(order=1)
@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self, setup):
        self.driver = setup
        self.login = Login(self.driver)

        self.login.verify_logo(Login.logo)
        print('1. Logo is visible, Passed!')

        self.login.verify_login_url(URL.site_url)
        print('2. Login Url is correct and verified, Passed!')

        userdata = DataJson.data

        for user in userdata:

            self.login.verify_email_field(Login.email, user['email'])
            self.login.verify_password(Login.password, user['password'])
            self.login.verify_login_btn()

            if user['expected'] == Login.expected_success_login:
                assert Login.expected_success_login in self.login.verify_success_login_message()
                print('7. Verify Login with valid Email and Password . Passed!')

            elif user['expected'] == Login.expected_invalid_password:
                assert Login.expected_invalid_password in self.login.verify_invalid_password_message()
                print('4. Verify Negative Test for Invalid Password, Passed!')

            elif user['expected'] == Login.expected_invalid_email:
                assert Login.expected_invalid_email in self.login.verify_invalid_email_message()
                print('3. Verify Negative Test for Invalid email, Passed!')

            elif user['expected'] == Login.expected_invalid_email_format:
                assert Login.expected_invalid_email_format in self.login.verify_invalid_email_format_message()
                print('5. Verify Negative Test for Invalid email without @ sign, Passed!')

            elif user['expected'] == Login.expected_no_email_input:
                assert Login.expected_no_email_input in self.login.verify_invalid_no_input()
                print('6. Verify Negative Test for Invalid no email input, Passed!')

        self.login.verify_dashboard_url()
        print('8. Dashboard Url is correct and verified, Passed!')
        print('9. User is Successfully login to Dashboard, Passed ')
