# Список моделей автомобилей
import random
from threading import Barrier, BrokenBarrierError, Thread
from time import sleep

car_models = ["Toyota", "BMW", "Audi", "Mercedes", "Ford", "Honda", "Nissan", "Chevrolet", "Volkswagen", "Kia"]


# Функция, симулирующая гонку автомобиля
def car_race(car_model, barrier: Barrier):
    try:
        barrier.wait()
        race_time = random.random() * 5
        sleep(race_time)
        print(f"Автомобиль {car_model} финишировал за {race_time:.2f} секунд")
    except Exception as e:
        print(e)


# Создание и запуск потоков для каждой модели автомобиля
def main():
    barrier = Barrier(len(car_models))
    for car_model in car_models:
        Thread(target=car_race, args=(car_model, barrier)).start()

if __name__ == '__main__':
    main()