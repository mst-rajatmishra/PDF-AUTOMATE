# PDF Form Filler Project

## Overview

The PDF Form Filler tool is designed to automate the process of filling PDF forms using JSON data and a configurable lookup table. The tool consists of two main components:

1. **JSON PDF Mapping**: The component in `tablemaker1.py` allows the user to create and configure lookup table mappings, which automate the process of filling a PDF form. This mapping links specific JSON fields to the PDF form fields.

2. **PDF Writer**: The component in `priv_look_work1.py` allows the user to test the form-filling process using the lookup table created in the JSON PDF Mapping tab. This tool fills the PDF form based on the mappings provided.

Included in the project are:
- An example fillable PDF form: `form_App Application 2024.pdf`
- An example provider data structure: `data.json`
- An example lookup table: `lookup_table.json`

## Directory Structure
```plaintext
PRIVILEGING_look/
│
├── data.json                    # JSON file containing the provider data to fill the form
├── filled_form.pdf              # Example of a filled PDF form
├── find_fields.py               # Script to find fields in the PDF
├── form_App Application 2024.pdf  # The target fillable PDF form
├── junk_collection/             # Temporary or auxiliary files
├── lookup_table.json            # JSON mapping file for form field paths
├── myenv/                       # Python virtual environment for this project
│   ├── bin/                     # Executables for the virtual environment
│   ├── include/                 # C headers of the environment
│   ├── lib/                     # Libraries for the virtual environment
│   └── pyvenv.cfg               # Configuration file for the environment
├── priv_look_work1.py           # Lookup table handling script for PDF filling
├── tablemaker1.py               # Main script to configure lookup table mappings
└── testmap.json                 # A test mapping JSON for testing purposes
```

## Setup

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd PRIVILEGING_look
```

### Step 2: Set Up the Python Environment

The project uses a virtual environment named `myenv` to ensure all required dependencies are installed. Here’s how to activate and use it:

1. Navigate to the `myenv` directory:

   ```bash
   cd myenv
   ```

2. Activate the environment:

   - On macOS/Linux:

     ```bash
     source bin/activate
     ```

   - On Windows:

     ```bash
     .\Scripts\activate
     ```

   Your terminal prompt will now show that `myenv` is activated:

   ```bash
   (myenv) username@computername myenv %
   ```

### Step 3: Install Dependencies

In case additional dependencies need to be installed, you can do so inside the environment:

```bash
pip install -r requirements.txt
```

### Step 4: Running the Scripts

Once the environment is activated, you can run any of the scripts in the repository. For example, to run the `tablemaker1.py` script:

```bash
python3.10 tablemaker1.py
```

### Step 5: Deactivate the Virtual Environment

When you’re done, you can deactivate the environment by running:

```bash
deactivate
```

## Usage

### Configuring the Lookup Table (JSON PDF Mapping)

The `tablemaker1.py` script allows users to configure the lookup table, which automates the mapping between the `data.json` file and the PDF fields. To run it:

```bash
python3.10 tablemaker1.py
```

