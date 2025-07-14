# Напишите свой код
from concurrent.futures import ThreadPoolExecutor


def task1():
    for i in range(5):
        print(i + 1)


def task2():
    for i in range(ord('a'), ord('e') + 1):
        print(chr(i))


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        t1 = executor.submit(task1)
        t2 = executor.submit(task2)

        t1.result()
        t2.result()

    print('Готово!')


if __name__ == '__main__':
    main()
