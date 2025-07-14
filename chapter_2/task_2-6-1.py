# Напишите простую функцию, которая принимает 2 аргумента: имя и время выполнения задачи.
# Функция должна имитировать работу в течение переданного ей времени работы и возвращать ее имя.
# Используйте пул потоков. Получите и выведите результаты тех задач, время выполнения которых длится менее 1.5 секунд.
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]


def worker(name: str, time: float):
    sleep(time)
    return name

def main():
    # threads = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        threads = [executor.submit(worker, name, time) for name, time in data]
        done, not_done = wait(threads, timeout=1.5)

        for thread in done:
            print(thread.result())


if __name__ == '__main__':
    main()