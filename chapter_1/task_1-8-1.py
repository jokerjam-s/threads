# Функция задачи для потоков
import threading
from time import sleep


code_names = [
    "Alpha", "Bravo", "Delta", "Star"
]

def task(code_name):

    sleep(2)
    print(f'Задача выполнена для {threading.current_thread().name}')

# Список кодовых имен
# Полный список вшит в задачу
# code_names = []

threads_list = []

def main():
    for name in code_names:
        thread = threading.Thread(target=task, args=(name,))
        print(f"Исходное имя потока: {thread.name}")
        thread.name = name
        print(f"Новое имя потока: {name}")
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()


if __name__ == '__main__':
    main()
