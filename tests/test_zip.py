from zipfile import ZipFile, ZIP_DEFLATED
import os
import pathlib
from conftest import path_tmp, path_resources

'''Создать новые тесты, которые заархивируют имеющиеся в resources различные 
типы файлов в один архив в tmp и проверят тестом в архиве каждый из файлов, 
что он является тем самым, который был заархивирован, не распаковывая архив.'''

path_zip = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))


def is_exist_zip(name, namelist):
    for item in namelist:
        if item == name:
            return True
    return False


def test_create_zip():
    source = os.listdir(path_resources)

    with ZipFile(os.path.join(path_zip, 'new.zip'), 'w', ZIP_DEFLATED) as archive:
        for file in source:
            add_file = os.path.join(path_resources, file)
            archive.write(add_file, arcname=file)

    assert os.path.exists(os.path.join(path_zip, 'new.zip'))

    with ZipFile(os.path.join(path_zip, 'new.zip')) as archive:
        assert len(source) == len(archive.infolist())

        files_list = archive.namelist()
        counter = 0
        for name in source:
            if is_exist_zip(name, files_list):
                counter += 1
        assert counter == len(source)

    os.remove(os.path.join(path_zip, 'new.zip'))
