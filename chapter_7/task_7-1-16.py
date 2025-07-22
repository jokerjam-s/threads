import os
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Event

import requests
from bs4 import BeautifulSoup


def scan_dir(path):
    result = []
    for root, dirs, files in os.walk(path):
        result.extend([os.path.join(root, name) for name in files])
    return result


def find_secret(file_path: str, event: Event):
    if event.is_set():
        return None

    with open(file_path) as f:
        url = f.read()

    responce = requests.get(url)
    if responce.status_code != 200:
        return None

    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    secret = soup.select_one('.secret-code p')
    if secret is not None:
        secret = secret.text
        event.set()

    return secret


event = Event()
list_files = scan_dir('.\\files')

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(find_secret, file, event) for file in list_files]

    wait(futures)

    for future in futures:
        if future.result() is not None:
            print(future.result())