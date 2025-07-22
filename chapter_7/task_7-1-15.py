# import threading
from concurrent.futures import ThreadPoolExecutor

import bs4
from requests import get
from bs4 import BeautifulSoup


def get_links(file_name: str) -> list:
    result = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result.append(line.replace('\n', ''))
    return result


def get_words_amount(url: str) -> int:
    html = get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'lxml')
        text = soup.text.replace('\n', ' ')
        return len(text.split())
    else:
        return 0

# words_amount = []

urls = get_links('generated_links.txt')
print(urls)
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(get_words_amount, url) for url in urls]
    words_amount = [f.result() for f in  futures]

    print(words_amount)
    print(sum(words_amount))




