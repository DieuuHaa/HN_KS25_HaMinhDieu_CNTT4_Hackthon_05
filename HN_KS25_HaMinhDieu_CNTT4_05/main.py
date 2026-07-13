from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
from schemas import CreateBook, UpdateBook
from services import create_book_service, get_all_book_service, search_book_service, get_book_by_id_service, update_book_service, delete_book_service
from exceptions import book_not_found
Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "API đang chạy",
        "data": None
    }

@app.post("/books")
def create_(book: CreateBook,db: Session = Depends(get_db)):
    new_book = create_book_service(db, book)
    return {
        "message": "Thêm sách mới thành công",
        "status_code": 201,
        "data": new_book
    }

@app.get("/books")
def get_all_(db: Session = Depends(get_db)):
    books = get_all_book_service(db)
    return {
        "message": "Success",
        "data": books
    }

@app.get("/books/search")
def search_book(keyword: str,db: Session = Depends(get_db)):
    books = search_book_service(db, keyword)
    return {
        "message": "Success",
        "data": books
    }

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int,db: Session = Depends(get_db)):
    book = get_book_by_id_service(db, book_id)
    if book is None:
        book_not_found()
    return {
        "message": "Success",
        "data": book
    }

@app.put("/books/{book_id}")
def update_book(book_id: int,book: UpdateBook,db: Session = Depends(get_db)):
    book_update = update_book_service(db, book_id, book)
    if book_update is None:
        book_not_found()
    return {
        "message": "Cập nhật thành công",
        "data": book_update
    }

@app.delete("/books/{book_id}")
def delete_book(book_id: int,db: Session = Depends(get_db)):
    result = delete_book_service(db, book_id)
    if result is False:
        book_not_found()
    return {
        "message": "Xóa thành công",
        "status_code": 200,
        "data": None,
    }