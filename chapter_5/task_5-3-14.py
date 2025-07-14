import time
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Event

clients = ["Виктор", "Ирина", "Андрей"]


def client_come_in(client: str, cassa_state: Event):
    print(f'{client} вошел в банк')
    while not cassa_state.is_set():
        cassa_state.wait(1)
    cassa_work(client, cassa_state)
    print(f'{client} обслужен и покидает банк')


def cassa_work(client: str, cassa_state: Event):
    cassa_state.clear()
    print(f'Обслуживаю клиента {client}')
    time.sleep(1.5)
    print(f'Клиент {client} обслужен')
    cassa_state.set()


def main():
    cassa_free = Event()
    cassa_free.set()

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(client_come_in, client, cassa_free) for client in clients]
        wait(futures)

    print('Все клиенты обслужены. Банк закрывается.')

if __name__ == '__main__':
    main()
