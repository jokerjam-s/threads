# Имитация функции обработки данных, которая может вызывать исключения
import random
import threading
from concurrent.futures import ThreadPoolExecutor

local = threading.local()
lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


def process_data(item):
    local.item = item
    # Имитация возможности возникновения ошибки
    if random.random() < 0.2:  # 20% шанс на ошибку
        raise ValueError(f"Ошибка обработки элемента {item}")
    return item  # Простая обработка данных


def callback(future):
    if future.exception():
        th_print(f"Элемент {local.item} вызвал ошибку: {future.exception()}")
    else:
        th_print(f"Элемент {future.result()} обработан успешно.")


# Список данных для обработки
data = [i for i in range(1, 21)]


def main():
    # Использование ThreadPoolExecutor для обработки данных
    with ThreadPoolExecutor(max_workers=2) as executor:
        for item in data:
            future = executor.submit(process_data, item)
            future.add_done_callback(callback)


if __name__ == '__main__':
    main()
