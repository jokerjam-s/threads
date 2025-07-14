import threading
from time import sleep

delays = [6, 2, 3, 4, 1, 2, 1, 4, ]


def my_task(delay):
    print(f"Поток {threading.current_thread().name} начал работу")
    sleep(delay)
    print(f"Поток {threading.current_thread().name} завершил работу")


def main():
    for delay in delays:
        threading.Thread(target=my_task, args=(delay,)).start()

    sleep(1.5)

    my_threads = threading.enumerate()
    for t in my_threads:
        print(f"{t.name} еще выполняется")


if __name__ == "__main__":
    main()
