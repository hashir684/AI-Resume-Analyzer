import os
import pdfplumber
from docx import Document


def extract_text_pdf(pdf_path):
    """
    Extract text from a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        print(f"[INFO] PDF pages detected: {len(pdf.pages)}")
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_text_doc(doc_path):
    """
    Extract text from a DOCX resume.

    Args:
        doc_path (str): Path to the DOCX file.

    Returns:
        str: Extracted text from the DOCX.
    """
    text = ""

    doc = Document(doc_path)
    print(f"[INFO] DOCX paragraphs detected: {len(doc.paragraphs)}")

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text.strip()


def extract_resume_text(file_path):
    """
    Detect resume file type and extract text accordingly.

    Args:
        file_path (str): Path to resume file (PDF or DOCX).

    Returns:
        str: Extracted resume text.

    Raises:
        ValueError: If unsupported file format is provided.
    """

    name, ext = os.path.splitext(file_path)
    ext = ext.lower()

    print(f"[INFO] Detected file type: {ext}")

    if ext == ".pdf":
        return extract_text_pdf(file_path)
    elif ext == ".docx":
        return extract_text_doc(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX allowed.")
