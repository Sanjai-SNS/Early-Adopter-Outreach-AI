# chains/utils.py

import requests
from bs4 import BeautifulSoup

def fetch_and_clean_text(urls):
    texts = []
    for url in urls:
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            texts.append(text[:2000])  # Limit length
        except Exception:
            continue
    return texts
