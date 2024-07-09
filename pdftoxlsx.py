import pdfplumber
import pandas as pd


def extract_table_from_pdf(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize an empty list to hold all rows of the table
        all_data = []

        # Loop through each page in the PDF
        for page in pdf.pages:
            # Extract tables from the page
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    all_data.append(row)

        # Return the extracted data
        return all_data


def clean_and_structure_data(data):
    # Remove any rows with only None values or empty strings
    cleaned_data = [row for row in data if any(
        cell is not None and cell != '' for cell in row)]

    # Convert to DataFrame
    df = pd.DataFrame(cleaned_data)

    # Assume the first row is the header
    df.columns = df.iloc[0]
    df = df[1:]

    # Reset index for a clean DataFrame
    df.reset_index(drop=True, inplace=True)

    return df


def convert_pdf_to_excel(pdf_path, excel_path):
    data = extract_table_from_pdf(pdf_path)
    df = clean_and_structure_data(data)
    df.to_excel(excel_path, index=False)
    print(f"Excel file saved to {excel_path}")


# Example usage
pdf_path = 'path_to_your_bank_statement.pdf'
excel_path = 'output_bank_statement.xlsx'
convert_pdf_to_excel(pdf_path, excel_path)
