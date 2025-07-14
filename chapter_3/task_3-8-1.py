import threading
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

data = {1.4: 'ljeo', 0.4: 'akwx', 2.3: 'tydx', 2.7: 'qnai', 2.6: 'smgx',
        1.9: 'fhef', 1.6: 'wzag', 2.5: 'hjsz', 2.4: 'gpay', 0.5: 'wxco'}

lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


def work(time: float, name: str):
    sleep(time)
    th_print(f'Задача {name} выполнилась.')


def main():
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(work, t, n) for t, n in data.items()]

        for i, t in enumerate(data.keys()):
            if t * 10 % 2 != 0:
                futures[i].cancel()

        wait(futures)


if __name__ == '__main__':
    main()
