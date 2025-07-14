# Определите функцию для обработки числа. Если число меньше или равно семи, то необходимо вычислить его факториал,
# если больше - его квадрат. Функция должна сообщать о начале обработки числа, в виде:
#           Обработка числа <число> началась
#
#           затем должна имитировать время работы, в виде задержки в 1/10 секунды от передаваемого числа и в заключении
#           возвращать необходимый результат вычислений;
#
# Используйте ручное управление пулом потоков;
# По завершению вычислений выведите в консоль сумму полученных результатов в виде:
#           Сумма обработанных чисел равна <результат>
import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep

numbers = [19, 1, 4, 13, 10, 7, 16]
lock = threading.Lock()


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def square(number):
    return number ** 2


def th_print(message):
    with lock:
        print(message)


def worker(number):
    th_print(f'Обработка числа {number} началась')
    sleep(number / 10)
    return square(number) if number > 7 else factorial(number)


def main():
    executor = ThreadPoolExecutor()
    futures = [executor.submit(worker, n) for n in numbers]

    executor.shutdown(wait=True)
    print(f'Сумма обработанных чисел равна {sum([f.result() for f in futures])}')


if __name__ == '__main__':
    main()
