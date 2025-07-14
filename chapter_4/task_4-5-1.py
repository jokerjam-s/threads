import queue
import threading
from threading import Thread
from time import sleep

electronics = ["смартфон", "ноутбук", "планшет", "камера", "гарнитура",
               "телевизор", "гаджет", "монитор", "роутер", "плеер"]

sklad = queue.Queue(maxsize=5)
lock = threading.Lock()

def th_print(message):
    with lock:
        print(message)

def sender():
    i = 0
    while i < len(electronics):
        try:
            sklad.put(electronics[i], block=False)
            th_print(f'Поставлен товар: {electronics[i]}')
            i = i + 1
        except queue.Full:
            th_print('Склад временно заполнен')
        sleep(0.5)
    th_print('Поставки закончились')


def saler():
    while True:
        sleep(1)
        item = sklad.get()
        th_print(f'Продан товар: {item}')
        sklad.task_done()


def main():
    prod = Thread(target=sender, daemon=True)
    sale = Thread(target=saler, daemon=True)
    prod.start()
    sale.start()

    sklad.join()

if __name__ == '__main__':
    main()