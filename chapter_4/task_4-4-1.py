import queue
import threading
import time

# Блокировка для потокобезопасного вывода в консоль.
lock = threading.Lock()

electronics = [(1, "смартфон"), (15, "ноутбук"), (7, "планшет"), (33, "камера"), (67, "гарнитура"),
               (4, "телевизор"), (21, "гаджет"), (83, "монитор"), (0, "роутер"), (47, "плеер")]

# Приоритетная очередь.
priority_queue = queue.PriorityQueue(maxsize=5)


# Функция для извлечения элемента очереди
def extractor():
    while True:
        el = priority_queue.get()
        time.sleep(el[0] / 100)
        # Потокобезопасная печать
        with lock:
            print(f'Обработан "{el[1]}"')
        priority_queue.task_done()


def producer():
    for item in electronics:
        loader(item)


# Функция для постановки элемента в очередь
def loader(seq):
    priority_queue.put(seq)



th_prod = threading.Thread(target=producer, daemon=True)
th_ext_1= threading.Thread(target=extractor, daemon=True)
th_ext_2 = threading.Thread(target=extractor, daemon=True)

th_prod.start()
th_ext_1.start()
th_ext_2.start()

priority_queue.join()


