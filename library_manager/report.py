from library_manager.catalog import Library

def generate_report(library: Library) -> str:
    report = "Books:\n" + "\n".join(f"{i}: {book}" for (i, book) in enumerate(sorted(library.list_books(), key=lambda book: book.title), start=1))
    return report
