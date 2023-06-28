import csv
import os

from conftest import path_resources

# оформить в тест, добавить ассерты и использовать универсальный путь

path_to_csv = os.path.join(path_resources, 'eggs.csv')


def test_csv():
    with open(path_to_csv, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

        assert os.path.exists(path_to_csv)

    with open(path_to_csv) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3

    os.remove(path_to_csv)
