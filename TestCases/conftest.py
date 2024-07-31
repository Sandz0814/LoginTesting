import pytest
from selenium import webdriver
from TestData.data import URL


@pytest.fixture(scope="class")
def setup(request):
    # Initialize Chrome options
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Edge(options=options)
    driver = webdriver.Edge()
    driver.get(URL.site_url)
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver

    driver.close()
    driver.quit()


def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: mark a test as a sanity test")
    config.addinivalue_line("markers", "run(order: int): mark a test to run in a specific order")
    config.addinivalue_line("markers", "regression: mark a test as a regression test")
    config.addinivalue_line("markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')")
    config.addinivalue_line("markers", "serial")

