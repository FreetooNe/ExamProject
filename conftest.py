import datetime
import os.path

import pytest
from pages.start_page import StartPage
from pages.utils import create_driver, log_wrapper


@pytest.fixture()
def driver(browser):
    """Create selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Create start page object"""
    return StartPage(driver)


