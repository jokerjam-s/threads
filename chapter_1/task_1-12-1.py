# Словарь с моделями самолетов и временем полета
# Полный словарь вшит в задачу
import threading
from time import sleep

aircrafts = {
    'Boeing 737': 6,
    'Airbus A320': 9,
    'Boeing 747': 6,
    'Airbus A380': 7,
}


# Функция для печати сообщений о начале и завершении полета.
def flight_simulation(model, flight_time):
    print(f"{model} начал полет. Время полета: {flight_time} сек.")
    sleep(flight_time)
    print(f"{model} завершил полет.")


def main():
    for model, flight_time in aircrafts.items():
        threading.Thread(target=flight_simulation, args=(model, flight_time)).start()

    sleep(5)
    print(f"Количество самолетов в воздухе после 5 секунд: {threading.active_count() - 1}")


if __name__ == '__main__':
    main()
