# WebHarvest: Web Content Scraper and Analyzer

WebHarvest is a powerful Python tool for extracting and processing web content. It enables users to scrape websites, extract meaningful text content, and combine results into a single document for analysis.

## Features

- **Single-page scraping**: Extract content from a specific URL
- **Recursive crawling**: Follow links within the same domain up to a specified depth
- **Content extraction**: Pull out titles, paragraphs, and code blocks while ignoring navigation and other non-content elements
- **Content combination**: Merge multiple scraped pages into a single document
- **Clean formatting**: Output is saved as structured text files with proper markdown formatting

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/WebHarvest.git
cd WebHarvest

# Install dependencies
pip install -r requirements.txt
```

## Dependencies

- requests
- beautifulsoup4

## Usage

### Single URL Scraping

To scrape a single URL without following links:

```bash
python single.py
```

This launches an interactive prompt where you can enter URLs to scrape. Type "quit" to exit.

### Recursive Website Crawling

To crawl a website by following links up to a specified depth:

```bash
python main.py
```

You'll be prompted to enter a starting URL and maximum crawl depth.

### Combining Scraped Content

After scraping, combine all extracted content into a single file:

```bash
python combine.py
```

By default, this takes files from the `base` directory and outputs to `combine/combine.txt`. You can customize these paths by modifying the function call.

## How It Works

1. **Scraping**: The tool fetches web pages, parses the HTML, and extracts meaningful content
2. **Content Extraction**: It focuses on extracting titles, paragraphs, and code blocks while ignoring navigation and other non-content elements
3. **File Storage**: Each page is saved as a separate text file named after the URL
4. **Combination**: The separate files can be combined into a single document for easier analysis

## Customization

- Modify the `extract` function in `main.py` to customize what elements are extracted
- Adjust timeouts and other request parameters in the scraping functions
- Change output directories by modifying the function parameters

