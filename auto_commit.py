import os
import time
from datetime import datetime

# Путь к файлу, который будет редактироваться
FILE_PATH = "file.txt"

# Интервал между коммитами (в секундах)
COMMIT_INTERVAL = 5

# Функция для добавления символа в файл
def append_character_to_file(file_path):
    with open(file_path, "a") as f:
        f.write("A")  # Добавляем символ 'A' в файл

# Основной цикл
while True:
    try:
        # Добавляем символ в файл
        append_character_to_file(FILE_PATH)

        # Добавляем файл в Git
        os.system(f'git add "{FILE_PATH}"')

        # Делаем коммит с текущей датой и временем в сообщении
        commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        os.system(f'git commit -m "{commit_message}"')

        # Пушим изменения на GitHub
        os.system("git push")

        # Ожидаем перед следующим коммитом
        time.sleep(COMMIT_INTERVAL)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        break
