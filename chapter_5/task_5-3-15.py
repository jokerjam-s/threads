# Событие для старта аукциона
import threading

auction_start = threading.Event()


# Функция, представляющая участника аукциона
def bidder(name):
    print(f"Участник {name} готов к аукциону.")
    auction_start.wait()
    print(f"Участник {name} делает ставку на редкую картину.")


# Имена участников аукциона
bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]


# Создание потоков-участников и запуск потоков
def main():
    for name in bidder_names:
        thread =threading.Thread(target=bidder, args=(name,))
        thread.start()

    print("Аукцион начинается!")
    auction_start.set()


if __name__ == '__main__':
    main()
