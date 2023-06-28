import os
import requests

from conftest import path_tmp

# оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь

path_png = os.path.join(path_tmp, 'selenium_logo.png')
url = 'https://selenium.dev/images/selenium_logo_square_green.png'


def test_download_png_with_api():
    response = requests.get(url)
    with open(path_png, 'wb') as file:
        file.write(response.content)

    assert os.path.exists(path_png)

    with open(path_png, 'rb') as file:
        selenium_png = file.read()
        print(len(selenium_png))

    size = os.path.getsize(path_png)
    assert size == 30803

    os.remove(path_png)
