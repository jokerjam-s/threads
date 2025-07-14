# Список для хранения сообщений
import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep

result_lst = []

# Список уникальных ID для потоков
unique_task_ids = ['StarExplorer42', 'QuantumLeap89', 'CyberWizard77',
                   'GalacticVoyager66', 'MysticCoder11', 'NeuralNinja53',
                   'QuantumRanger88', 'SpaceSurfer15', 'TimeTraveler23',
                   'CosmicSage99']


# Функция инициализации для потоков
def thread_initializer():
    print(f'Инициализация потока {threading.current_thread().name}')

# Функция, выполняемая потоками
def thread_task(task_id):
    sleep(1)
    return f'Поток {threading.current_thread().name} выполняет задачу {task_id}'

def main():
    # Создание пула потоков с функцией инициализации
    with ThreadPoolExecutor(max_workers=3, initializer=thread_initializer) as executor:
        for t in unique_task_ids:
            result_lst.append(executor.submit(thread_task, t))

    # Вывод списка с результатами работы потоков
    for r in result_lst:
        print(r.result())

if __name__ == '__main__':
    main()

