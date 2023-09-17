def src_book(id:int, books:list):
    for book in books:
        if id  == book.id:
            return book

def update_id(books, new_book):
    index = len(books)
    new_book.id = index + 1
    return new_book

def book_to_delete(id, books):
    for book in books:
        if id  == book.id:
            books.pop(id - 1)
    return books