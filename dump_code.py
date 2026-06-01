import os

# Добавил твою папку drf-py3.13 в список игнорирования
IGNORE_DIRS = {'venv', '.git', '__pycache__', 'migrations', '.idea', 'env', 'drf-py3.13'}
IGNORE_FILES = {'db.sqlite3', 'manage.py', 'dump_code.py', '.gitignore', 'project_code.txt'}
ALLOWED_EXTENSIONS = {'.py', '.html'}


def generate_code_dump(output_file="project_code.txt"):
    with open(output_file, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk("."):
            # Исключаем ненужные папки
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            # Жесткая проверка: если в пути есть папки библиотек Python, полностью их скипаем
            if "site-packages" in root or "Lib" in root or "Include" in root:
                continue

            for file in files:
                if file in IGNORE_FILES:
                    continue

                ext = os.path.splitext(file)[1]
                if ext in ALLOWED_EXTENSIONS:
                    relative_path = os.path.relpath(os.path.join(root, file))

                    out.write(f"\n\n{'=' * 40}\n")
                    out.write(f"FILE: {relative_path}\n")
                    out.write(f"{'=' * 40}\n\n")

                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            out.write(f.read())
                    except Exception as e:
                        out.write(f"[Ошибка чтения файла: {e}]\n")


if __name__ == "__main__":
    generate_code_dump()
    print("Готово! Теперь в файле остался только твой личный код.")