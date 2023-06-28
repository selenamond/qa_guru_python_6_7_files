import time
import os

from selene import browser
from conftest import path_tmp

# оформить в тест, добавить ассерты и использовать универсальный путь к tmp

path_to_file = os.path.join(path_tmp, 'pytest-main.zip')


def test_download_file_with_ui(driver_tmp_directory):
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(5)

    assert os.path.exists(path_to_file)
    os.remove(path_to_file)
