import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen

urls = ['https://asyncio.ru/multithreading/zadachi/6.2/1/1XhKkbDD.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/7S2gWnLv.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/g277YKL0.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/I1HtO6Mq.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/IhOYyvOe.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/M1wlL6jq.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/M3ifGSqg.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/tEWbv18D.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/usMtkqVB.txt',
        'https://asyncio.ru/multithreading/zadachi/6.2/1/x2Ifki9M.txt']


def download_file(url: str):
    filename = url.split('/')[-1]
    try:
        with urlopen(url) as response:
            return (response.read(), filename)
    except:
        print(f'Ошибка получения файла {filename}')
    return (None, filename)


def save_file(filename, data, path):
    outpath = os.path.join(path, filename)
    with open(outpath, 'wb') as file:
        file.write(data)
    return outpath


# Введите имя первого скачанного файла в значении переменной file_name
file_name = ''

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(download_file, url) for url in urls]

    for future in as_completed(futures):
        if future.result()[0] is not None:
            save_file(future.result()[1], future.result()[0], '.\\downloaded')
            if file_name == '':
                file_name = future.result()[1]

print(f"Первый скачанный файл: {file_name}")
