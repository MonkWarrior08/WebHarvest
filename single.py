import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse
from main import clean_file, extract

def scrape(url, base="base"):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = extract(soup)
    os.makedirs(base, exist_ok=True)
    filename = clean_file(url)
    filepath = os.path.join(base, filename)

    with open(filepath, 'w', encoding= 'utf-8') as f:
        f.write(f"source: {url}")
        f.write(content)

if __name__ == "__main__":
    while True:
        url = input("input url: ")
        if url.lower() == "quit":
            print("cancel")
            break
        scrape(url)
        print("finished")