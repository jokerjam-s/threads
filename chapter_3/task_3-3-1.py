from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

data = [(1, "Python"), (2, "Java"), (3, "Go"), (4, "JavaScript"), (5, "C++"),
        (6, "TypeScript"), (7, "PHP"), (8, "Ruby"), (9, "C"), (10, "C#")]


def worker(lang_info: tuple):
    place = lang_info[0]
    lang = lang_info[1]
    sleep(place/10)
    return f'{lang} на {place}-м месте на GitHub в первом квартале 2024 года'


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(worker, d) for d in data]

        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    main()
