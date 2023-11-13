import requests

def fetch_and_save_html(link, filename='tempPage.html'):
    """
    Fetches HTML content from the given link and stores it in a file.

    Parameters:
    - link: The URL of the web page to fetch.
    - filename: The name of the file to save the HTML content (default is 'tempPage.html').
    """
    try:
        # Fetch HTML content from the link
        response = requests.get(link)
        response.raise_for_status()  # Check for errors in the HTTP response

        # Save HTML content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"HTML content successfully fetched and saved to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML content: {e}")

# Example usage:
url_to_fetch = 'https://www.example.com'
fetch_and_save_html(url_to_fetch)
