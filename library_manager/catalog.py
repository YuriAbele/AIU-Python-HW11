#######################################################
# В реальной жизни классы Book и Library будут находиться
# в отдельных модулях, например, book.py и library.py
#######################################################

from .utils import * # Демонстрация __init__.py => __all__ из подпакета utils

class Book:
    """
    Класс для книги.
    С т.зр. ООП правильнее использовать этот класс, чем анонимный dict.
    При этом Book сам себя проверит на валидность и
    выдаст форматированное представление в виде строки - __str__ или даже __repl__
    """
    def __init__(self, title: str, author: str, genre: str):
        self.title = title.strip()
        self.author = author.strip()
        self.genre = genre.strip()

        # if(not self.is_valid): <= USE THIS FOR CORRECT OOP
        if(not validate_book_data({
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
        })):
            raise ValueError("Данные книги не валидны!")

    @property
    def is_valid(self) -> bool:
        """
        Getter-свойство для проверка данных книги
        """
        if self.title and self.author and self.genre:
            return True
        return False

    def validate_data_using_util(self) -> bool:
        """
        Исключительно для демонстрации импортирования [utils]
        В остальных случаях надо использовать не внешнюю, а ООП-нут само-проверку (свойство is_valid)
        """
        result = validate_book_data({
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
        })
        return result

    def __str__(self) -> str:
        """
        Исключительно для демонстрации импортирования [utils]
        В остальных случаях надо использовать не внешнюю функцию, а, с т.зр. правильного ООП, заставить объект самого себя описать
        """
        external_format = format_book_data({
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
        })
        return external_format
        # Расскомментировать для правильного ООП:
        # return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

    def __repr__(self) -> str:
        return f"Book(title=\"{self.title}\", author=\"{self.author}\", genre=\"{self.genre}\")"

class Library:
    """
    - Добавления книги (с атрибутами: название, автор, жанр).
    - Удаления книги по названию.
    - Поиска книги по названию, автору и жанру.
    - Просмотра всех книг в библиотеке.
    """

    # Скрываем прямой доступ к списку книг
    _books: list[Book] = [] # думал сделать на основе словаря (dict), но тогда не смогу хранить книги с одинаковым названием

    def __init__(self):
        pass

    def list_books(self) -> list[Book]:
        return self._books

    def add_book(self,
                 title: str,
                 author: str,
                 genre: str # жанр - по хорошему должен быть enum
                 ) -> None:
        """Добавляет книгу в библиотеку."""
        book = Book(title, author, genre) # на всякий случай, в самом конструкторе, будут убраны пробелы в начале и конце
        self._books.append(book)
        return book # на всякий случай возвращаем добавленную книгу

    def remove_book_by_title(self, title: str):
        """Удаляет книги по названию. При этом удаляются все книги с таким названием (регистр не важен)."""
        self._books = [book for book in self._books if book.title.lower() != title.strip().lower()] # самый "питоновский" способ, но не самый эффективный. Если бы было много книг, то лучше бы использовать filter + lambda

    def find_books_by_title(self, title: str) -> list[Book]:
        """Ищет книги по названию. Возвращает список книг с таким названием (регистр не важен)."""
        result = [book for book in self._books if book.title.lower() == title.strip().lower()]
        return result

    def find_books_by_author(self, author: str) -> list[Book]:
        result = [book for book in self._books if book.author.lower() == author.lower()]
        return result

    def find_books_by_genre(self, genre: str) -> list[Book]:
        result = [book for book in self._books if book.genre.lower() == genre.lower()]
        return result

