# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup: Initialize Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Quit after test
    driver.quit()
