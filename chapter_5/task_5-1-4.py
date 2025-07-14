import threading
from time import sleep

# Расширяем список видов пицц и время их приготовления
# Полный словарь вшит в задачу
dishes = {
    'Алексей': {'Маргарита': 3, 'Лазанья': 5, 'Креветочная': 4, 'Мидии в сливках': 4, 'Сицилийская': 5},
    'Иван': {'Мексиканская': 3, 'Вегетарианская': 4},
    'Василий': {'Мексиканская': 3, 'Вегетарианская': 4},
    'Дмитрий': {'Маргарита': 3, 'Лазанья': 5, 'Креветочная': 4, 'Мидии в сливках': 4, 'Сицилийская': 5},
    'Тимофей': {'Маргарита': 3, 'Лазанья': 5, 'Креветочная': 4, 'Мидии в сливках': 4, 'Сицилийская': 5},
    'Марина': {'Мексиканская': 3, 'Вегетарианская': 4},
    'Петр': {'Мексиканская': 3, 'Вегетарианская': 4},
}


def get_locks(count: int):
    for _ in range(count):
        yield threading.Lock()


def cook_dish(cook_name: str, dish: dict):
    for dish_name, dish_time in dish.items():
        processing = True
        while processing:
            for oven in ovens_lock:
                if oven.acquire(False):
                    print(f'{cook_name} начал(а) готовить {dish_name}, время приготовления {dish_time} сек.')
                    sleep(dish_time)
                    oven.release()
                    print(f'{cook_name} закончил(а) готовить {dish_name}, заняло {dish_time} сек.')
                    processing = False
                    break
            if processing:
                sleep(0.2)


ovens_lock = [l for l in get_locks(5)]


def main():
    for cook, dish in dishes.items():
        threading.Thread(target=cook_dish, args=(cook, dish)).start()


if __name__ == '__main__':
    main()
