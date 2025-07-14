import threading
import time

# Создаем объект мьютекса
oven_lock = threading.Lock()

# Список видов пицц и время их приготовления
pizzas = {
    "Маргарита": 3,
    "Пепперони": 2,
    "Вегетарианская": 4,
    "Четыре сыра": 5,
    "Гавайская": 3
}

# Список имен поваров
cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]


def cook_pizza(name, pizza_name, pizza_time):
    oven_lock.acquire()
    print(f'{name} начал(а) готовить пиццу "{pizza_name}".')
    time.sleep(pizza_time / 10)
    print(f'{name} закончил(а) готовить пиццу "{pizza_name}".')
    oven_lock.release()


def main():
    threads = [
        threading.Thread(target=cook_pizza, args=(cook_name, pizza_name, pizza_time)) for
        cook_name, pizza_name, pizza_time in zip(cooks_names, [x for x in pizzas.keys()], [x for x in pizzas.values()])
    ]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Все пиццы приготовлены!")


if __name__ == '__main__':
    main()
