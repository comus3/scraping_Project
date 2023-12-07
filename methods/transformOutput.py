import ast,writeToCSV

def fetch_and_iterate():
    # Specify the file name
    file_name = "output.txt"

    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Convert the content to a dictionary using ast.literal_eval
            dictionary_data = ast.literal_eval(content)

            # Create a list from all values of all keys
            result_list = [value for values in dictionary_data.values() for value in values]

            return result_list

    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
        return None

def sendToCsvMaker(list):
    csvparser = ","
    outputStr = ""
    for email in list:
        outputStr = outputStr + csvparser + email
    writeToCSV.write_to_csv(outputStr)
    
sendToCsvMaker(fetch_and_iterate())