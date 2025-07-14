import time
from asyncio import as_completed
from concurrent.futures import TimeoutError as FutureTimeoutError, ThreadPoolExecutor, wait
from time import sleep


# Функция, которая будет выполняться в каждом потоке
def process_number(timeout, number):
    time.sleep(timeout)  # Имитация длительной задачи
    return number


# Список таймаутов и список чисел
timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [2257, 6217, 6594, 2259, 5284, 3568, 1741, 5462, 7494, 8971, 3157, 3998, 2040, 8828, 8769, 6976, 9367, 1267,
           6255, 7322]


#
# def main():
#     # Создаем список для хранения результатов
#     results = []
#
#     # Создаем ThreadPoolExecutor
#     with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
#         futures = [executor.submit(process_number, timeouts[i], numbers[i]) for i in range(len(numbers))]
#
#         sleep(3)
#
#         for future in futures:
#             if future.done() and not future.cancelled():
#                 results.append(future.result())
#
#     # Выводим результаты
#     print(sum(results))
#     print(results)
#     print(len(results), len(numbers))


def main():
    # Создаем список для хранения результатов
    results = []

    # Создаем ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
        futures = [executor.submit(process_number, timeouts[i], numbers[i]) for i in range(len(numbers))]

        wait(futures, timeout=3, return_when="FIRST_EXCEPTION")

        for future in futures:
            if future.done() and not future.cancelled():
                results.append(future.result())

    # Выводим результаты
    print(sum(results))


if __name__ == '__main__':
    main()
