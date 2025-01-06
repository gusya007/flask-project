import os

# Указываем структуру проекта
structure = {
    "project": [
        "project",
        "project/app",
        "project/app/static",
        "project/app/templates",
        "project/tests"
    ],
    "files": [
        "project/app/__init__.py",
        "project/app/routes.py",
        "project/requirements.txt",
        "project/.travis.yml",
        "project/main.py"
    ]
}

# Функция для создания папок
def create_folders(base_path, folders):
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Создана папка: {path}")

# Функция для создания файлов
def create_files(base_path, files):
    for file in files:
        file_path = os.path.join(base_path, file)
        # Убедимся, что папка для файла существует
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            pass  # Создаем пустой файл
        print(f"Создан файл: {file_path}")

# Базовая папка проекта
base_folder = "."

# Создаем структуру проекта
create_folders(base_folder, structure["project"])
create_files(base_folder, structure["files"])

print("Структура проекта успешно создана.")
