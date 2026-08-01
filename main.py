from fastapi import FastAPI, HTTPException
from schemas import *
app = FastAPI()

book = {
  "title": "Dế Mèn Phiêu Lưu Ký",
  "author": "Tô Hoài",
  "price": 45000,
  "pages": 200
}

books_db = []

@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    new_book = {
        "id": len(books_db) + 1,
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "pages": book.pages
    }
    books_db.append(new_book)
    return new_book

@app.get("/books/{id}",response_model=BookResponse)
def get_book_by_id(id: int):
    for i in books_db:
        if i["id"] == id:
            return i
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

