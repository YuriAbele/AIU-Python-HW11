import sys
import os

# 1. Получаем путь к текущему файлу (tests/__init__.py)
current_path = os.path.dirname(os.path.abspath(__file__))
# 2. Поднимаемся на один уровень вверх, чтобы получить корень репозитория
root_path = os.path.dirname(current_path)
# 3. Добавляем корневой путь в sys.path, если его там еще нет
if root_path not in sys.path:
    sys.path.append(root_path)

from library_manager import Library, generate_report

def test_nested_imports():
	library = Library()
	library.add_book("Алиса в стране чудес", "Льюис Кэрролл", "Сказка, литература абсурда")
	library.add_book("Маленький принц", "Антуан де Сент-Экзюпери", "Философская сказка-аллегория")
	library.add_book("Золотая цепь", "Александр Грин", "Роман, приключения")

	print(generate_report(library))


__all__ = ["test_nested_imports"]