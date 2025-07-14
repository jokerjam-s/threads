# Список идентификаторов для именования потоков
import threading
import time

name_threads = ['OF95RK', 'VH61DX', 'NB03WA', 'WO40ZF', 'NJ48EG', 'SX21ET', 'AT01PA', 'MR36DD', 'DD84HR', 'MI81QY']

def worker():
    # Получите имя текущего потока, не передавая аргументов, и верните необходимое сообщение
    thread_name = threading.current_thread().name
    print(thread_name + ' начал работу.')
    time.sleep(1)
    print(thread_name + ' завершил работу.')

# Создайте и запустите 10 потоков
threads_list = list()
for name in name_threads:
    t = threading.Thread(target=worker, name=f'Name_thread-{name}')
    threads_list.append(t)

for t in threads_list:
    t.start()

# Дождитесь завершения всех потоков
for t in threads_list:
    t.join()

