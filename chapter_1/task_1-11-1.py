# Инициализация параметров аукциона
import threading

initial_bid = 10     # Начальная ставка аукциона. С этой суммы начинается аукцион.
bid_increment = 2   # Сумма, на которую увеличивается текущая ставка на каждом шаге аукциона.
max_bid =  100        # Максимальная ставка, при достижении которой аукцион завершается.
interval = 1        # Интервал времени (в секундах) между увеличениями ставок.

current_bid = 0

# Допишите функцию увеличения ставки
def increase_bid():
    global current_bid
    if current_bid == 0:
        current_bid = initial_bid
    else:
        current_bid += bid_increment
        print(f"Текущая ставка: {current_bid} у.е.")

    if current_bid < max_bid:
        threading.Timer(interval, increase_bid).start()
    else:
        print('Ставок нет, аукцион завершен!')


# Вызовите эту функцию
def main():
    increase_bid()

if __name__ == '__main__':
    main()