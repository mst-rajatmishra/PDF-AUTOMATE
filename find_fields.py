import fitz  # PyMuPDF

def extract_pdf_fields(pdf_path):
    pdf_document = fitz.open(pdf_path)
    fields = {}
    for page_num, page in enumerate(pdf_document, start=1):
        for widget in page.widgets():
            if widget.field_name:
                print(f"Field: {widget.field_name} (Page {page_num})")
                fields[widget.field_name] = widget
    return fields

def main():
    input_pdf_path = 'form_App Application 2024.pdf'
    pdf_fields = extract_pdf_fields(input_pdf_path)

if __name__ == "__main__":
    main()

