# scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_page_content(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_links(html: str, domain: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True) if domain in a['href']]

def extract_detailed_links(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        url = link['href']
        text = link.get_text(strip=True)
        links.append({'text': text, 'url': url})
    return links

def get_webpage_title(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.get_text(strip=True) if title_tag else ''

def parse_url(url: str):
    parsed = urlparse(url)
    return {'domain': parsed.netloc, 'path': parsed.path, 'scheme': parsed.scheme}