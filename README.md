PDF to Excel Converter

This project provides a Python script to convert PDF bank account statements to Excel files using pdfplumber for text extraction and pandas for data manipulation.


Requirements

Before running the script, ensure you have the following Python packages installed:

pdfplumber

pandas

openpyxl

You can install these packages using pip:

pip install pdfplumber pandas openpyxl


Usage

Clone the Repository

Clone this repository to your local machine:

git clone https://github.com/vishesh-allahabadi/pdf-to-excel-converter.git

cd pdf-to-excel-converter


Prepare Your PDF File

Place your PDF bank statement in the same directory as the script or provide the path to the PDF file.


Run the Script

Adjust File Paths

Replace 'path_to_your_pdf.pdf' with the path to your PDF file and 'output_excel.xlsx' with the desired output path for the Excel file.

Execute the script using Python:

python convert_pdf_to_excel.py


Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.


License

This project is licensed under the MIT License.

