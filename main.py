import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse

visited = set()

def clean_file(url):
    parsed = urlparse(url)
    filename = parsed.netloc + parsed.path
    filename = re.sub(r'[^a-zA-Z-0-9_.-]', "_", filename)
    filename += '.txt'
    return filename

def extract(soup):
    content = []
    if soup.title:
        content.append(f"# {soup.title.string.strip()}\n\n")

    for element in soup.find_all(['p', 'pre', 'code']):
        if element.name == 'p':
            content.append(element.get_text().strip() + "\n\n")
        elif element.name in ['pre', 'code']:
           content.append(f"```\n{element.get_text().strip()}\n```\n\n")

    
    return "".join(content)

def scrape(url, base="base"):
    global visited

    if url in visited:
        return []
    
    visited.add(url)

    try:
        response = requests.get(url, timeout=15)

        if 'text/html' not in response.headers.get('Content-Type', ''):
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        content = extract(soup)

        os.makedirs(base, exist_ok=True)

        filename = clean_file(url)
        filepath = os.path.join(base, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"source: {url}")
            f.write(content)
        print(f"saved {filepath}")

        new_link = []
        for link in soup.findAll('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)

            if urlparse(full_url).netloc == urlparse(url).netloc:
                new_link.append(full_url)
        return new_link
    
    except Exception as e:
        print(f"Error {url}: {e}")
        return []

def scrape_other(start_url, max= 2):
    to_visit = [(start_url, 0)]

    while to_visit:
        current, depth = to_visit.pop(0)
        print(f"scraping {current}, depth: {depth}")

        if depth > max:
            continue

        new_link = scrape(current)

        for link in new_link:
            if link not in visited:
                to_visit.append((link, depth+1))

if __name__ == "__main__":
    start_url = input("enter url: ")
    max = int(input("max depth: "))
    scrape_other(start_url, max)
    print(f"finished, total page: {len(visited)}")