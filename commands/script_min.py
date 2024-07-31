from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Command:

    def __init__(self, driver):
        self.driver = driver

    def find_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def find_css(self, selector):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
        return element

    def find_name(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, name)))
        return element

    def find_id(self, id):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, id)))
        return element

    def find_elements(self, xpath):
        sel1 = self.driver.find_element(By.XPATH, xpath)
        sel2 = self.driver.find_elements(By.XPATH, xpath)

        sel3 = []
        if sel1:
            sel3.append(sel1)
        sel3.extend(sel2)

        return sel3













