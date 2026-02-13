import fitz
import docx


def extract_text(raw_bytes, filename: str):
    extension = filename.lower().split(".")[-1]
    if extension == "pdf":
        doc = fitz.open(stream=raw_bytes, filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif extension == "docx":
        document = docx.Document(raw_bytes)
        return "\n".join(p.text for p in document.paragraphs)
    else:
        return raw_bytes.decode("utf-8", errors="ignore")
