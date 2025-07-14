# Напишите программу для симуляции работы кафе. У вас есть два потока - один представляет посетителей кафе,
# а другой - баристу, который готовит кофе. Посетители должны ожидать своего заказа, а бариста должен готовить кофе.
# Когда бариста заканчивает приготовление кофе, он оповещает посетителя, который забирает свой заказ.
# После того как все посетители получили свой кофе, программа должна завершиться с выводом в консоль:
#
# Все посетители получили свой кофе. Работа завершена.
import threading
from queue import Queue
from threading import Condition
from time import sleep

visitors = ["Алиса", "Владимир", "Сергей"]


class Cafe:
    """Объект обслуживания - кафе."""

    def __init__(self):
        self.orders = Queue()
        self.condition = Condition()

    def make_visit(self, visiters: list):
        """Запускаем посетителей в кафе."""
        for visitor in visiters:
            threading.Thread(target=self.make_order, args=(visitor,)).start()
        barista = threading.Thread(target=self.barista)
        barista.start()
        barista.join()
        print('Все посетители получили свой кофе. Работа завершена.')

    def make_order(self, name: str):
        """Посетитель заказывает кофе."""
        print(f'{name} зашел в кафе')
        self.orders.put_nowait(name)
        with self.condition:
            self.condition.wait()
        print(f'{name} получил свой кофе')

    def barista(self):
        """Бариста готовит кофе."""
        while not self.orders.empty():
            order = self.orders.get_nowait()
            print(f'Готовим кофе для {order}')
            sleep(2)
            print(f'Кофе для {order} готов')
            with self.condition:
                self.condition.notify()
            sleep(1)


def main():
    cafe = Cafe()
    cafe.make_visit(visitors)


if __name__ == '__main__':
    main()
