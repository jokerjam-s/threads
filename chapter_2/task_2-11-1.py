
fifty = ['OF95RK', 'VH61DX', 'NB03WA', 'OL41DZ']
one_hundred = ['JF39XW', 'RO06QB', 'RW48XW', 'ZE42EF']
two_hundred = ['FP99WI', 'IJ21HS', 'SV16JN', 'EP11JG']

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


# Функция для вывода сообщения
def process_element(elem, pool_size):
    return f"Элемент {elem} списка из пула размером {pool_size}"


# Функция для создания и использования пула потоков
def process_with_threadpool(elements, pool_size) -> ThreadPoolExecutor:
    with  ThreadPoolExecutor(max_workers=pool_size) as executor:
        futures = [executor.submit(process_element, elem, pool_size) for elem in elements]

        for e in as_completed(futures):
            th_print(e.result())


def main():
    # Обработка списков с разными размерами пулов
    process_with_threadpool(fifty, 50)
    process_with_threadpool(one_hundred, 100)
    process_with_threadpool(two_hundred, 200)


if __name__ == '__main__':
    main()
