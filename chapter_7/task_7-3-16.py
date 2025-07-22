import threading
from concurrent.futures import ThreadPoolExecutor
from itertools import product

elements = ["#fW", "^1a", "!b2", "l(3", "#5R", "e%1", "3Ff", "=b1", "vF^", "-F0"]
lock = threading.Lock()


def compare_element(element):
    # Эталонный элемент
    reference_element = "=b1#5Re%1"

    # Сравнение переданного элемента с эталоном
    if element == reference_element:
        return f"Элемент совпал = {element}"
    else:
        raise ValueError(f"Элемент {element} не совпадает с эталоном.")


def safe_print(text):
    with lock:
        print(text)


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(compare_element, "".join(element)) for element in product(elements, repeat=3)]

    for future in futures:
        try:
            result = future.result()
            safe_print(result)
        except Exception as e:
            safe_print(e)
