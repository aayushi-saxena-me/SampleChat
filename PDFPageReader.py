import fitz  # PyMuPDF
import json


# Path to the PDF file
pdf_path = "/Users/rashmi.srivastava/Downloads/LAW-Spring24-issuu.pdf"

# Open and read the PDF
with fitz.open(pdf_path) as pdf_document:
    filename = "underformer_guide.txt"
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]  # Get each page
        print(f"--- Page {page_num + 1} ---")
        #print(page.get_text())
        with open(filename, 'a') as file:
            json.dump(page.get_text(), file, indent=4)  # Store in pretty JSON format
