from fastapi import Body, FastAPI
from data import books
from models import BookRequest, Book
from apiTools import *


app = FastAPI(
    title="Api Biblioteca",
    version="0.0.1",
    description="Api de Biblioteca, Pydantic",
)

@app.get('/books')
async def get_books():
    return books

@app.get('/book/{id}')
async def get_by_id(id: int):
    return src_book(id, books)

@app.post('/new-book')
async def post_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(book_request)
    return books
