from methods import accessPage,createLinks,findDataValues,findMail,writeToCSV
import json


def write_dict_to_file(dictionary, filename='output.txt'):
    """
    Write a dictionary to a text file in JSON format.

    Parameters:
    - dictionary: The dictionary to be written to the file.
    - filename: The name of the file (default is 'output.txt').
    """
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


def run_fetch_and_save_with_retry(link, max_retries=5):
    print("fetching html for {}".format(link))
    for _ in range(max_retries):
        result = accessPage.fetch_and_save_html(link)
        if result == 1:
            print("Retrying...")
        elif result == 0:
            print("Fetching and saving HTML successful.")
            return findMail.extract_emails_from_html()
        else:
            print("Error fetching and saving HTML.")
            break
    print("Max retries exceeded.")
    return None

locations = findDataValues.createLocationLinks()
linkList = createLinks.createLinkList(locations)

csvParser = ","
output = ""

for link in linkList:
    for email in run_fetch_and_save_with_retry(link):
        output = output + csvParser + email
print(output)
writeToCSV.write_to_csv(output)



# output = {}

# index = 0
# for link in linkList:
#     output[locations[index]] = run_fetch_and_save_with_retry(link)
#     index = index + 1
    
# write_dict_to_file(output)
