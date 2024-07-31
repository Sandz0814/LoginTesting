import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://admin-demo.nopcommerce.com/login')

time.sleep(5)

logo = driver.find_element(By.XPATH, "//h1[normalize-space()='Admin area demo']")
logo_text = logo.text
assert "Admin area demo" in logo_text

email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.clear()
time.sleep(2)
email.send_keys('admin@yourstore.com')
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@id='Password']")
password.clear()
time.sleep(2)
password.send_keys('admin')
time.sleep(3)

login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
login_btn.click()

logout = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").is_displayed()

if logout:
    print('User Successfully logging in')
    assert True










