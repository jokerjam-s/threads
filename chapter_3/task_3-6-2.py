import threading
from concurrent.futures import ThreadPoolExecutor

devices = [
    {"name": "Server1", "ip": "192.168.1.1", 'status': True},
    {"name": "Router1", "ip": "192.168.1.2", 'status': True},
    {"name": "Switch1", "ip": "192.168.1.3", 'status': False},
    {"name": "Server10", "ip": "192.168.1.28", 'status': True},
    {"name": "Router10", "ip": "192.168.1.29", 'status': False},
    {"name": "Switch10", "ip": "192.168.1.30", 'status': True}
]

lock = threading.Lock()


def th_print(message):
    with lock:
        print(message)


# Функция для мониторинга устройства
def monitor_device(device: dict):
    th_print(f"Мониторинг устройства: {device['name']}, с IP {device['ip']} статус: {device['status']}")
    return device


# Функция обратного вызова для обработки результата мониторинга
def handle_device_status(future):
    if not future.exception():
        device = future.result()
        if device['status']:
            th_print(f"Устройство {device['name']} активно и работает нормально.")
        else:
            th_print(f"Внимание: Устройство {device['name']} неактивно! Включаем устройство.")
            device['status'] = True
            th_print(f"Устройство {device['name']} успешно включено!")


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for device in devices:
            future = executor.submit(monitor_device, device)
            future.add_done_callback(handle_device_status)


if __name__ == '__main__':
    main()
