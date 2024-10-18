import json
import fitz  # PyMuPDF

# Load the JSON data
def load_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

# Load the lookup table
def load_lookup_table(lookup_file):
    with open(lookup_file, 'r') as file:
        return json.load(file)

# Extract value from JSON using the JSON path
def extract_value_from_json(json_data, json_path):
    keys = json_path.split(' -> ')
    for key in keys:
        print(f"Accessing key '{key}' in JSON data")
        if isinstance(json_data, list):
            try:
                key = int(key[1:-1]) if key.startswith('[') and key.endswith(']') else int(key)
                json_data = json_data[key]
            except (ValueError, IndexError) as e:
                print(f"Error accessing key '{key}': {e}")
                return None
        else:
            json_data = json_data.get(key)
            if json_data is None:
                print(f"Key '{key}' not found in JSON.")
                return None
    return json_data

# Fill PDF form fields using data from JSON and lookup table
def fill_pdf(input_pdf_file, output_pdf_file, json_data, lookup_table):
    pdf_document = fitz.open(input_pdf_file)
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        for field in page.widgets():
            field_name = field.field_name
            if field_name in lookup_table:
                json_path = lookup_table[field_name]['json_path']
                field_type = lookup_table[field_name]['type']
                field_value = extract_value_from_json(json_data, json_path)
                
                if field_type == "FILL_FIELD":
                    if field_value:
                        field.field_value = field_value
                        field.update()
                        print(f"Filling {field_name} with {field_value}")

                elif field_type == "FILL_ADDRESS":
                    if isinstance(field_value, dict):
                        address_parts = [
                            field_value.get("Street1 :"),
                            field_value.get("Street2 :"),
                            field_value.get("City :"),
                            field_value.get("State :"),
                            field_value.get("Zip Code :")
                        ]
                        address = ', '.join([part for part in address_parts if part])
                        field.field_value = address
                        field.update()
                        print(f"Filling {field_name} with {address}")

                elif field_type == "CHECKBOX":
                    allowed_values = lookup_table[field_name]['allowed_values']
                    if field_value and field_value in allowed_values:
                        field.field_value = field_value
                        field.update()
                        print(f"Checking {field_name} with {field_value}")
                        
                elif field_type == "RADIO_BUTTON":
                    allowed_values = lookup_table[field_name]['allowed_values']
                    if field_value and field_value.upper() in allowed_values:
                        if field_value.upper() == "YES":
                            field.field_value = "Yes"
                        elif field_value.upper() == "NO":
                            field.field_value = "No"
                        field.update()
                        print(f"Selecting {field_name} with {field.field_value}")

    pdf_document.save(output_pdf_file)

# Main function
def main():
    input_pdf_file = "form_App Application 2024.pdf"
    output_pdf_file = "output.pdf"
    json_data_file = "data.json"
    lookup_table_file = "lookup_table.json"
    
    # Load data from JSON and lookup table
    json_data = load_json(json_data_file)
    print("JSON Data:", json_data)  # Check loaded JSON data
    lookup_table = load_lookup_table(lookup_table_file)
    print("Lookup Table:", lookup_table)  # Check loaded lookup table

    # Fill the PDF
    fill_pdf(input_pdf_file, output_pdf_file, json_data, lookup_table)

# Run the main function
if __name__ == "__main__":
    main()
