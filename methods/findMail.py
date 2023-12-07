import re
from bs4 import BeautifulSoup

def extract_emails_from_html(filename="tempPage.html"):
    """
    Extracts email addresses from an HTML file for a specific region.

    Parameters:
    - filename: The name of the HTML file to be opened.

    Returns:
    - emails: List of email addresses found in the HTML file.
    """
    emails = []

    try:
        # Read the HTML content from the file
        with open(filename, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all occurrences of "mailto:" in the HTML content
        mailto_links = soup.find_all(href=re.compile(r'^mailto:'))

        # Extract and filter email addresses based on the specified region
        for link in mailto_links:
            email_address = re.search(r'mailto:(.*?)"', str(link)).group(1)
            emails.append(email_address)

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error processing HTML file: {e}")

    return emails

# # Example usage:
# html_filename = 'tempPage.html'
# result_emails = extract_emails_from_html(html_filename)

# print("Email addresses for the specified region:")
# for email in result_emails:
#     print(email)
