import threading
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

data = [('CPU', 3.1), ('RAM', 1.5), ('GPU', 1.6), ('Motherboard', 1.8), ('SSD', 1.3),
        ('Keyboard', 1.5), ('Mouse', 3.9), ('Monitor', 2.8), ('Headphones', 3.0), ('Router', 1.0)]

lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


def work(name: str, time: float):
    sleep(time)
    th_print(f'Задача {name} выполнилась за {time} секунды')


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(work, *d) for d in data]

        for future in futures:
            future.cancel()

        wait(futures)


if __name__ == '__main__':
    main()
