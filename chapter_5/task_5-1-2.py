import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def write_jsno(data):
    file_lock.acquire()
    with open('data.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
    file_lock.release()


file_lock = threading.Lock()
files_list = [
    'first_name.txt',
    'last_name.txt',
    'age.txt',
    'country.txt',
    'hobbies.txt',
    'salary.txt',
    'job_title.txt',
    'email.txt',
    'projects.txt',
    'education.txt',
]
data_lists = []

for file in files_list:
    with open(os.path.join('./txt', file), 'r') as f:
        data = [d for d in f.read().split('\n')]

    if len(data_lists) > 0:
        for i in range(len(data)):
            data_lists[i][file.split('.')[0]] = data[i]
    else:
        for i in range(len(data)):
            data_lists.append({file.split('.')[0]: data[i]})

json.dump(data_lists, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False)

# print(data_lists)
