import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# Список уникальных имен клиентов
name_list = [
    "Клиент Веселый Шутник",
    "Клиент Читающий Поэт",
    "Клиент Спешащий Бизнесмен",
    "Клиент Мечтающий Путешественник",
    "Клиент Меланхоличный Художник",
    "Клиент Загадочная Улыбка",
    "Клиент Задумчивый Философ",
    "Клиент Вечно Опаздывающий",
    "Клиент Гадающий на Кофейной Гуще",
    "Клиент Неугомонный Блогер"
]

# Семафор для имитации доступности столов в кафе
cafe_semaphore = threading.Semaphore(3)

# Основная функция работник
def client(client_name):
    with cafe_semaphore:
        print(f'{client_name} нашел свободный столик и заказывает кофе')
        # sleep(.5)
    print(f'{client_name} насладился кофе и освобождает столик для следующих гостей')

# Запуск потоков-клиентов
with ThreadPoolExecutor(max_workers=10) as executor:
    threads = [executor.submit(client, name) for name in name_list]
