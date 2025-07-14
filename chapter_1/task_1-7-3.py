import threading
from time import sleep

file_names = ['file623.xlsx', 'file538.jpg', 'file11.rar', 'file180.jpg', 'file984.docx',
              'file931.rar', 'file600.zip', 'file928.jpg', 'file899.pdf', 'file763.png',
              'file601.txt', 'file194.pdf', 'file307.rar', 'file961.jpg', 'file539.mp4',
              'file44.docx', 'file276.zip', 'file387.zip', 'file520.xlsx', 'file516.mp3',
              'file802.jpg', 'file708.mp3', 'file100.xlsx', 'file327.xlsx', 'file451.zip',
              'file125.pdf', 'file477.jpg', 'file432.pdf', 'file569.docx', 'file990.mp3',
              'file688.mp3', 'file735.docx', 'file505.txt', 'file650.docx', 'file445.png',
              'file963.mp4', 'file583.pdf', 'file403.xlsx', 'file406.pdf', 'file187.txt',
              'file13.zip', 'file495.docx', 'file47.png', 'file491.rar', 'file506.zip',
              'file960.docx', 'file95.mp3', 'file566.jpg', 'file66.rar', 'file13.txt']

res = []

# Функция для имитации загрузки файла
def load_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f'{thread_name} начал загрузку файла {file_name}.')
    sleep(1)
    res.append(f'{thread_name} завершил загрузку файла {file_name}.')

# Функция для имитации обработки файла
def process_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f'{thread_name} начал обработку файла {file_name}.')
    sleep(3)
    res.append(f'{thread_name} завершил обработку файла {file_name}.')


# Функция для имитации сохранения файла
def save_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f'{thread_name} начал сохранение файла {file_name}.')
    sleep(1)
    res.append(f'{thread_name} завершил сохранение файла {file_name}.')

threads = []
# Допишите код
for file_name in file_names:
    thread = threading.Thread(target=load_file, args=(file_name,), name=f'LoadThread-{file_name}')
    threads.append(thread)
    thread.start()
    thread = threading.Thread(target=process_file, args=(file_name,), name=f'ProcessThread-{file_name}')
    threads.append(thread)
    thread.start()
    thread = threading.Thread(target=save_file, args=(file_name,), name=f'SaveThread-{file_name}')
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for rs in res:
    print(rs)
