import pymupdf

def extract_pdf_text(pdf_file):
    document = pymupdf.open(stream=pdf_file.getvalue(), filetype="pdf")

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()
    return extracted_text

# print(extract_pdf_text("sports_classification_sample.pdf"))