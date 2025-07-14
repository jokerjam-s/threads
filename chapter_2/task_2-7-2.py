import threading
from concurrent.futures import ThreadPoolExecutor
from itertools import cycle
from time import sleep

lock = threading.Lock()


def get_unique_thread_id():
    unique_thread_ids = ['KFD34',
                         'DGS6D',
                         'F7F9S',
                         'SDG0D',
                         'WQ9WE',
                         '29AXC',
                         'AF632',
                         'DCV13',
                         'Q9ETF',
                         '1D0S3']

    thread_ids = cycle(unique_thread_ids)
    # Допишите возврат уникального значения из списка unique_thread_ids при обращении к функции
    yield from thread_ids


id_gen = get_unique_thread_id()


def safe_print(s):
    with lock:
        print(s)


# Функция инициализации потока, должна выводить определённое сообщения
def thread_initializer():
    safe_print(f'Инициализация потока: {next(id_gen)}')


# Задача worker, должна выводить два сообщение
def thread_task(num):
    safe_print(f'Задача {num} запущена')
    sleep(0.1)
    safe_print(f'Задача {num} выполнена')


def main():
    # Создайте пул потоков с инициализацией потоков и их запуском
    with ThreadPoolExecutor(max_workers=10, initializer=thread_initializer) as executor:
        executor.map(thread_task, range(10))


if __name__ == '__main__':
    main()
