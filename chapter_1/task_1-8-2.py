# Словарь имен потоков и их миссий
# Полный словарь вшит в задачу
import random
from threading import Thread
import time

missions = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
}

threads = list()

# Описание задачи для потоков
def mission(mission_name):
    print(f'[{mission_name}] Миссия началась.' )
    time.sleep(random.randint(1, 3))
    print(f'[{mission_name}] Миссия успешно выполнена!' )


def main():
    for thread_name, mission_name in missions.items():
        thread = Thread(target=mission, args=(mission_name,), name=thread_name)
        threads.append(thread)
        print(f"[{thread_name} ({mission_name})] Статус миссии до запуска: {thread.is_alive()}")
        thread.start()
        print(f"[{thread_name} ({mission_name})] Миссия активна: {thread.is_alive()}")

    for thread in threads:
        thread.join()

    for thread in threads:
        print(f"[{thread.name} ({missions[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")

if __name__ == '__main__':
    main()