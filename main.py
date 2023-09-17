import sys
import uuid
import os
import random
import time
import threading
from tqdm import tqdm
from github import Github
from rockstar import RockStar

# Устанавливаем кодировку вывода для терминала
sys.stdout.reconfigure(encoding='utf-8')


# Функция для создания временного файла
def create_temp_file(file_name):
    with open(file_name, "w") as file:
        file.write("")  # Создаем пустой файл


# Функция для выполнения обратного отсчета
def countdown_timer(seconds):
    for i in tqdm(range(seconds)):
        time.sleep(1)


# Функция для проверки изменений на GitHub
def check_for_changes(repo):
    while True:
        commits = repo.get_commits()
        if commits:
            print("Замечены новые изменения на GitHub.")
        else:
            print("Новых изменений на GitHub не замечено.")
        time.sleep(60)


# Функция для выполнения случайных действий
def perform_random_action():
    for day in range(1, num_days + 1):
        print(f"День {day}:")
        random_action = random.choice(daily_actions[day])
        print(f"Выполняется действие: {random_action}")

        if random_action == "Создать новый Python-файл":
            # Генерируем случайное имя файла
            random_filename = str(uuid.uuid4()) + ".py"
            # Создаем файл с случайным именем
            with open(random_filename, "w") as new_file:
                new_file.write("print('Hello, world!')")

        elif random_action == "Добавить новые строки в файл README.md":
            # Генерируем рандомное количество строк (от 1 до 5)
            num_lines = random.randint(1, 5)
            # Создаем или открываем файл README.md для добавления строк
            with open("README.md", "a") as readme:
                for _ in range(num_lines):
                    random_text = str(uuid.uuid4())  # Генерируем случайный текст
                    readme.write("\n" + random_text)
        elif random_action == "Изменить файл requirements.txt":
            # List of libraries and their versions
            libraries = [
                "library1==1.0.0",
                "library2==2.0.0",
                "library3==3.0.0",
                "library3==3.0.0",
                "library3==3.0.1",
                "library3==3.0.2",
                "library3==3.0.3",
                "library3==3.0.4",
                "library3==3.0.5",
                "library3==3.0.6",
            ]
            # Generate a random number of libraries (1 to 5)
            num_libraries = random.randint(1, 5)
            # Create or open the requirements.txt file to add libraries
            with open("requirements.txt", "a") as requirements:
                for _ in range(num_libraries):
                    random_library = random.choice(libraries)  # Choose a random library
                    requirements.write("\n" + random_library)
        elif random_action == "Создать новую ветку":

            # Генерация случайного имени для ветки (например, "feature/day_3")
            branch_name = f"feature/day_{random.randint(1, 95)}"

            # Команда для создания новой ветки в Git
            git_command = f"git checkout -b {branch_name}"
            os.system(git_command)
        elif random_action == "Добавить и отправить изменения на GitHub":
            os.system("git add .")
            os.system("git commit -m 'Добавление изменений'")
            os.system("git push")
        elif random_action == "Выполнить команду git checkout master":
            os.system("git checkout master")
        elif random_action == "Создать файл notes.txt":
            # Генерация случайного имени файла (например, "notes_123.txt")
            file_name = f"notes_{random.randint(1, 1000)}.txt"

            # Список случайных строк
            random_content = [
                "Это случайная строка 1",
                "Это случайная строка 2",
                "Это случайная строка 3",
                "Это случайная строка 4",
                "Это случайная строка 5",
                "Это случайная строка 6",
                "Это случайная строка 7",
                "Это случайная строка 8",
                "Это случайная строка 9",
                "Это случайная строка 11",
            ]
            # Выбор случайного содержания из списка
            random_line = random.choice(random_content)
            # Создание файла с случайным содержанием
            with open(file_name, "w") as new_file:
                new_file.write(random_line)
        elif random_action == "Изменить файл .gitignore":
            # Список рандомных строк для добавления в .gitignore
            random_gitignore_lines = [
                "*.tmp",
                "*.log",
                "cache/",
                "temp/",
                "*.tmp",
                "*.log",
                "cache/",
                "temp/",
            ]

            # Выбор случайной строки из списка
            random_gitignore_line = random.choice(random_gitignore_lines)
            # Открываем файл .gitignore для добавления
            with open(".gitignore", "a") as gitignore:
                gitignore.write("\n" + random_gitignore_line)
        elif random_action == "Исправить баг 123":
            os.system("git checkout -b bugfix/123")
            os.system("echo 'Исправление бага 123' >> bugfix.txt")
            os.system("git add .")
            os.system("git commit -m 'Исправление бага 123'")
            os.system("git push --set-upstream origin bugfix/123")
        elif random_action == "Создать RockStar программу":
            create_rockstar_program()

        # Команды Git
        print("Выполняется команда git push...")
        os.system("git add .")
        os.system("git commit -m 'Добавление изменений'")

        # Проверяем наличие изменений перед отправкой
        git_status = os.popen("git status --porcelain").read()
        if git_status.strip():
            os.system("git push")
            print("Изменения отправлены на GitHub.")
        else:
            print("Нет изменений для отправки на GitHub.")
        print(f"Следующее действие через {interval} минут")



    print("Все действия выполнены в течение 5 дней. Скрипт завершает работу.")


# Функция для создания RockStar программы
def create_rockstar_program():
    print("Генерируется RockStar программа...")
    # Генерируем случайное имя файла для RockStar программы
    file_name = f"rockstar_program_{random.randint(1, 1000)}.rock"
    # Создаем объект RockStar с заданным количеством строк (от 1 до 5)
    rock_program = RockStar(days=random.randint(1, 5))
    # Записываем программу в файл
    with open(file_name, "w") as rock_file:
        rock_file.write(rock_program.make_me_a_rockstar())
    print(f"RockStar программа сохранена в файле {file_name}")


# Введите ваш логин GitHub
username = input("Введите ваш логин GitHub: ")

# Введите ваш персональный токен доступа GitHub
token = input("Введите ваш персональный токен доступа GitHub: ")

# Создаем объект GitHub
g = Github(username, token)

# Введите URL своего репозитория (например, https://github.com/username/repository)
repo_url = input("Введите URL вашего репозитория на GitHub: ")

# Разбиваем URL репозитория на части
repo_parts = repo_url.split('/')
if len(repo_parts) != 5:
    print("Неверный формат URL репозитория. Укажите URL в формате https://github.com/username/repository")
else:
    username, repo_name = repo_parts[-2], repo_parts[-1]

    # Проверяем доступность репозитория
    try:
        repo = g.get_repo(f"{username}/{repo_name}")
        print(f"Репозиторий {repo_name} доступен.")

        daily_actions = {
            1: [
                "Создать новый Python-файл",
                "Выполнить команду git pull",
                "Создать RockStar программу",
            ],
            2: [
                "Добавить и отправить изменения на GitHub",
                "Создать файл notes.txt",
                "Изменить файл .gitignore",
            ],
            3: [
                "Случайное действие 1 для дня 3",
                "Случайное действие 2 для дня 3",
            ],
            4: [
                "Случайное действие 1 для дня 4",
                "Случайное действие 2 для дня 4",
            ],
            5: [
                "Случайное действие 1 для дня 5",
                "Случайное действие 2 для дня 5",
            ],
        }

        interval = int(input("Введите интервал между действиями (в минутах): "))
        num_days = 5

        action_thread = threading.Thread(target=perform_random_action)
        check_thread = threading.Thread(target=check_for_changes, args=(repo,))

        action_thread.start()
        check_thread.start()

        action_thread.join()
        check_thread.join()

    except Exception as e:
        print(f"Ошибка: {e}")
