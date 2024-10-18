# automates the process of filling out a PDF form using data sourced from a JSON file and a lookup table


import json
import fitz  # PyMuPDF
import argparse

# Load the JSON data
def load_json(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

# Load the lookup table
def load_lookup_table(lookup_path):
    with open(lookup_path, 'r') as file:
        return json.load(file)

# Extract value from JSON using the JSON path
def extract_value_from_json(json_data, json_path):
    keys = json_path.split(' -> ')
    for key in keys:
        print(f"Accessing key '{key}' in JSON data")
        if isinstance(json_data, list):
            try:
                # Handle list indices like [0]
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
def fill_pdf(input_pdf_path, output_pdf_path, json_data, lookup_table):
    pdf_document = fitz.open(input_pdf_path)
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

    pdf_document.save(output_pdf_path)

# Main function
def main():
    # Setup argparse to accept command-line arguments
    parser = argparse.ArgumentParser(description="Fill PDF form using JSON data and lookup table.")
    parser.add_argument("input_pdf_path", help="Path to the input fillable PDF form")
    parser.add_argument("output_pdf_path", help="Path to save the filled PDF form")
    parser.add_argument("json_data_path", help="Path to the provider JSON data file")
    parser.add_argument("lookup_table_path", help="Path to the lookup table file")
    
    args = parser.parse_args()

    # Load data from JSON and lookup table
    json_data = load_json(args.json_data_path)
    lookup_table = load_lookup_table(args.lookup_table_path)

    # Fill the PDF
    fill_pdf(args.input_pdf_path, args.output_pdf_path, json_data, lookup_table)

# Run the main function
if __name__ == "__main__":
    main()


