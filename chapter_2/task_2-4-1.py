# Напишите простую функцию, которая принимает 2 аргумента: имя и время выполнения задачи.
# Функция должна имитировать работу в течение переданного ей времени работы и возвращать ее имя.
# Используйте пул потоков. Получите и выведите результаты тех задач, время выполнения которых длится менее 1.5 секунд.
from concurrent.futures import ThreadPoolExecutor
from time import sleep

data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]


def worker(name: str, time: float):
    sleep(time)
    return name

def main():
    # threads = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for name, time in data:
            thread = executor.submit(worker, name, time)
            try:
                result = thread.result(timeout=1.5)
                print(result)
            except TimeoutError:
                thread.cancel()

if __name__ == '__main__':
    main()