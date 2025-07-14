# Списки официантов, поваров и блюд
import random
import threading
from queue import Queue
from threading import Condition
from time import sleep

waiters = ["Анна", "Иван", "Света"]
chefs = ["Шеф_Антон", "Шеф_Сергей", "Шеф_Георгий"]
dishes = ["Борщ", "Салат Цезарь", "Стейк", "Паста Карбонара", "Тирамису"]

# Создаем объект условия
condition = Condition()
q = Queue()


# Функция для официанта (главного потока)
def waiter(waiter_name):
    for _ in range(3):
        dish = random.choice(dishes)
        print(f"{waiter_name} передал заказ на {dish}")
        q.put_nowait(dish)


# Функция для повара (рабочего потока)
def chef(chef_name):
    with condition:
        condition.wait()
    while not q.empty():
        dish = q.get_nowait()
        print(f"{chef_name} готовит {dish}...")
        sleep(random.randint(10, 31) / 10)
        print(f"{chef_name} закончил готовить {dish}")


# Создаем и запускаем потоки официантов и поваров
for ch in chefs:
    threading.Thread(target=chef, args=(ch,)).start()

for wt in waiters:
    threading.Thread(target=waiter, args=(wt,)).start()

# Запускаем и ожидаем все потоки
with condition:
    condition.notify_all()
#
