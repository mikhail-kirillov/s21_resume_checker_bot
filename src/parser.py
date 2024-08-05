import os

import fitz


def read_pdf_file(path_to_file) -> str:
    with fitz.open(path_to_file) as file:
        text = ""
        for page in file:
            text += " ".join([i.strip() for i in str(page.get_text()).splitlines()])
    os.remove(path_to_file)
    return text
