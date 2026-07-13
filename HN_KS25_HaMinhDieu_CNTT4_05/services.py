from sqlalchemy.orm import Session
from models import LibraryModel

def create_book_service(db: Session, book):
    new_book = LibraryModel(
        title = book.title,
        author = book.author,
        category = book.category,
        quantity = book.quantity
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_all_book_service(db: Session):
    book = db.query(LibraryModel).all()
    return book

def get_book_by_id_service(db: Session, book_id: int):
    book = db.query(LibraryModel).filter(LibraryModel.id == book_id).first()
    return book

def update_book_service(db: Session, book_id: int, book):
    update= db.query(LibraryModel).filter(LibraryModel.id == book_id).first()
    if update is None:
        return None
    update.title= book.title
    update.author = book.author
    update.category = book.category
    update.quantity = book.quantity
    db.commit()
    db.refresh(update)
    return update

def delete_book_service(db: Session, book_id: int):
    book = db.query(LibraryModel).filter(LibraryModel.id == book_id).first()
    if book is None:
        return False
    db.delete(book)
    db.commit()
    return True

def search_book_service(db: Session, keyword: str):
    book = db.query(LibraryModel).filter(LibraryModel.name.like(f"%{keyword}%")).all()
    return book
