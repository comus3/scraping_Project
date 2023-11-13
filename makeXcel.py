import os
import pandas as pd
import json

def read_dict_from_file(filename='output.txt'):
    """
    Read a dictionary from a text file.

    Parameters:
    - filename: The name of the file to read the dictionary from (default is 'output.txt').

    Returns:
    - data_dict: The dictionary read from the file.
    """
    project_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(project_dir)
    file_path = os.path.join(parent_dir,"scraping_project", filename)

    try:
        with open(file_path, 'r') as file:
            data_dict = json.load(file)
        return data_dict
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def save_dict_to_excel(data_dict, excel_filename='output.xlsx'):
    """
    Save a dictionary to an Excel file.

    Parameters:
    - data_dict: The dictionary to be saved to the Excel file.
    - excel_filename: The name of the Excel file (default is 'output.xlsx').
    """
    project_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(project_dir)
    excel_path = os.path.join(parent_dir, 'scraping_Project', 'methods', excel_filename)

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data_dict.items(), columns=['Region', 'Email Addresses'])

    # Write the DataFrame to an Excel file
    df.to_excel(excel_path, index=False)

    print(f"Data successfully saved to {excel_path}")

# Example usage:
# Reading the dictionary from the 'output.txt' file
loaded_dict = read_dict_from_file()

if loaded_dict:
    # Saving the dictionary to an Excel file
    save_dict_to_excel(loaded_dict)
