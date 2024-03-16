# main.py
from urllib.parse import urlparse
from scraper import fetch_page_content, extract_links
from models import WebpageContent
from storage import create_minio_client, save_document

def process_webpage(url):
    content = fetch_page_content(url)
    links = extract_links(content, domain=urlparse(url).netloc)
    # Here you could parse the title and content more accurately using BeautifulSoup
    webpage_data = WebpageContent(url=url, title="Webpage Title", content=content[:100] + "...", links=links)
    return webpage_data

def main():
    url = "https://docs.anthropic.com/claude/docs/helper-metaprompt-experimental"
    data = process_webpage(url)
    minio_client = create_minio_client()
    domain = urlparse(url).netloc.replace(".", "-")
    path = urlparse(url).path.replace("/", "-").lstrip("-")
    save_document(minio_client, "knowledge-set", f"{domain}/{path}.txt", data.json(indent=4))

if __name__ == '__main__':
    main()