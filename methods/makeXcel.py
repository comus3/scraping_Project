import pandas as pd
def save_dict_to_excel(data_dict, excel_filename='output.xlsx'):
    """
    Save a dictionary to an Excel file.

    Parameters:
    - data_dict: The dictionary to be saved to the Excel file.
    - excel_filename: The name of the Excel file (default is 'output.xlsx').
    """
    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['Email Addresses'])

    # Write the DataFrame to an Excel file
    df.to_excel(excel_filename, index_label='Region')

    print(f"Data successfully saved to {excel_filename}")

