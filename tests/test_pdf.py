from pypdf import PdfReader
from conftest import path_resources
import os


# оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf_reader():
    pdf = PdfReader(
        os.path.join(path_resources, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(pdf.pages)
    assert number_of_pages == 412

    last_page = pdf.pages[411]
    last_page_text = last_page.extract_text()
    assert 'WarningsRecorder' in last_page_text
