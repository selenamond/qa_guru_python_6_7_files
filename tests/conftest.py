import os
import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

path_tmp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))
print(path_tmp)

path_resources = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../resources'))
print(path_resources)


@pytest.fixture(scope='function', autouse=False)
def driver_tmp_directory():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": path_tmp,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    browser.config.driver = driver
