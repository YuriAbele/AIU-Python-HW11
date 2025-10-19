def validate_book_data(data: dict) -> bool:
    is_title_ok = True if ("title" in data) and data["title"] else False
    is_author_ok = True if ("author" in data) and data["author"] else False
    is_genre_ok = True if ("genre" in data) and data["genre"] else False
    if is_title_ok and is_author_ok and is_genre_ok:
        return True
    return False
