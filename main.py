import os
import requests
from bs4 import BeautifulSoup

# Function to fetch and parse the HTML content of a webpage
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None

# Function to extract links to EPUB files from HTML content
def extract_epub_links(html_content):
    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Modify this part to match the HTML structure of the website
    epub_links = [a['href'] for a in soup.find_all('a', href=True, text='Download EPUB')]

    return epub_links

# Function to download EPUB files
def download_epub(url, destination_folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(destination_folder, url.split("/")[-1])
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Main function
def main():
    base_url = "http://example.com/page{}"  # Modify the URL structure accordingly
    destination_folder = "downloaded_epubs"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for page_number in range(1, 11):  # Loop through pages 1 to 10
        url = base_url.format(page_number)
        html_content = get_html_content(url)
        epub_links = extract_epub_links(html_content)

        for epub_link in epub_links:
            epub_url = f"{url}/{epub_link}"  # Adjust the URL formation based on your website structure
            download_epub(epub_url, destination_folder)

if __name__ == "__main__":
    main()
