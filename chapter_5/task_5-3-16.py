# Имена участников аукциона
import random
import threading

bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]

# Создайте события для старта каждого аукциона
auction_start_painting = threading.Event()
auction_start_clock = threading.Event()


# Функция участник аукциона за картину
def bidder_painting(name):
    print(f'Участник {name} готов к аукциону за редкую картину.')
    auction_start_painting.wait()
    print(f'Участник {name} делает ставку на редкую картину.')


# Функция участник аукциона за часы
def bidder_clock(name):
    print(f'Участник {name} готов к аукциону за антикварные часы.')
    auction_start_painting.wait()
    print(f'Участник {name} делает ставку на антикварные часы.')


def main():
    # Создание и запуск потоков-участников
    threads_painting = [threading.Thread(target=bidder_painting, args=(name,)) for name in bidder_names]
    threads_clock = [threading.Thread(target=bidder_clock, args=(name,)) for name in bidder_names]

    print("Аукцион за редкую картину начинается!")
    auction_start_painting.set()
    for t in threads_painting:
        t.start()
        t.join()
    print("Аукцион за редкую картину завершился!")

    print("Аукцион за антикварные часы начинается!")
    auction_start_clock.set()
    for t in threads_clock:
        t.start()
        t.join()
    print("Аукцион за антикварные часы завершился!")

    print(f'Победитель аукциона за редкую картину: {random.choice(bidder_names)}')
    print(f'Победитель аукциона за антикварные часы: {random.choice(bidder_names)}')

if __name__ == '__main__':
    main()
