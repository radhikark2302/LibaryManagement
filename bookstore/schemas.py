# api/schemas.py
from ninja import Schema
from datetime import date

class BookSchema(Schema):
    id: int
    title: str
    author: str
    published_date: date
    is_borrowed: bool

    class Config:
        orm_mode = True

class BookCreateSchema(Schema):
    title: str
    author: str
    published_date: date

class BorrowSchema(Schema):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: date = None

    class Config:
        orm_mode = True

class BorrowCreateSchema(Schema):
    user_id: int
    book_id: int
