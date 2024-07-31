import time
from commands.script_min import Command


class Login(Command):
    logo = "//h1[normalize-space()='Admin area demo']"
    email = "//input[@id='Email']"
    password = "//input[@id='Password']"
    login_btn = "//button[normalize-space()='Log in']"
    logout = "//a[normalize-space()='Logout']"

    success_login_message = "//a[normalize-space()='Logout']"
    invalid_email_message = "//li[normalize-space()='No customer account found']"
    invalid_password_message = "//li[normalize-space()='The credentials provided are incorrect']"
    invalid_email_format_message = "//span[@class='field-validation-error']"
    invalid_no_email_input = "//span[@id='Email-error']"

    expected_success_login = 'Logout'
    expected_invalid_password = 'The credentials provided are incorrect'
    expected_invalid_email = 'No customer account found'
    expected_invalid_email_format = 'Please enter a valid email address.'
    expected_no_email_input = 'Please enter your email'

    def verify_login_url(self, url):
        assert url in self.driver.current_url

    def verify_logo(self, selector):
        self.find_xpath(selector)

    def verify_email_field(self, selector, string):
        self.find_xpath(selector).clear()
        time.sleep(1)
        self.find_xpath(selector).send_keys(string)

    def verify_password(self, selector, string):
        self.find_xpath(selector).clear()
        time.sleep(1)
        self.find_xpath(selector).send_keys(string)

    def verify_login_btn(self):
        self.find_xpath(self.login_btn).click()

    def verify_logot_text_assertion(self, selector):
        logging_in_assertion = self.find_xpath(selector).is_displayed()
        if logging_in_assertion:
            print('User Successfully logged in')
            assert True

    def verify_dashboard_url(self):
        assert "https://admin-demo.nopcommerce.com/admin/" in self.driver.current_url

    def verify_invalid_password_message(self):
        invalid_password = self.find_xpath(self.invalid_password_message).text
        return invalid_password

    def verify_invalid_email_message(self):
        invalid_email = self.find_xpath(self.invalid_email_message).text
        return invalid_email

    def verify_invalid_email_format_message(self):
        invalid_email_format = self.find_xpath(self.invalid_email_format_message).text
        return invalid_email_format

    def verify_success_login_message(self):
        success_login_message = self.find_xpath(self.success_login_message).text
        return success_login_message

    def verify_invalid_no_input(self):
        invalid_no_input_message = self.find_xpath(self.invalid_no_email_input).text
        return invalid_no_input_message


