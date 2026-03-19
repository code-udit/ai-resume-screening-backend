# app/file_utils.py

from PyPDF2 import PdfReader


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(file_bytes)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    return text