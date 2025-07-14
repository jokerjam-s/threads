from concurrent.futures import ThreadPoolExecutor

messages = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]

# Функция для подсчета символов в строке
def count_characters(message: str):
    return len(message)

# Использование ThreadPoolExecutor для параллельного подсчета символов
def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        character_counts = list(executor.map(count_characters, messages))

    # Вывод результатов
    print(f"Общее количество символов в каждой строке: {character_counts}")

if __name__ == '__main__':
    main()