def src_book(id:int, books:list):
    for book in books:
        if id  == book.id:
            return book