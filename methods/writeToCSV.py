def write_to_csv(input_string):
    # Specify the file name
    file_name = "output.csv"
    
    try:
        # Open the file in write mode ('w')
        with open(file_name, 'w') as file:
            # Write the content of the string to the file
            file.write(input_string)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")
