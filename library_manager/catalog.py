#######################################################
# В реальной жизни классы Book и Library будут находиться
# в отдельных модулях, например, book.py и library.py
#######################################################

class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre # жанр

    # def __str__(self) # will use __repr__()

    def __repr__(self):
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
        book = Book(title.strip(), author.strip(), genre.strip) # на всякий случай убираем пробелы в начале и конце
        self._books.append(book)
        return book # на всякий случай возвращаем добавленную книгу

    def remove_book(self, title: str):
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

