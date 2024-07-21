
from ninja import NinjaAPI
from ninja.errors import HttpError
from .models import Book, Borrow
from .schemas import BookSchema, BookCreateSchema, BorrowSchema, BorrowCreateSchema
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from datetime import date

api = NinjaAPI()

@api.post("/books", response=BookSchema)
def add_book(request, data: BookCreateSchema):
    try:
        book = Book.objects.create(**data.dict())
        return book
    except Exception as e:
        raise HttpError(400, f"Error adding book: {str(e)}")

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, data: BookCreateSchema):
    try:
        book = get_object_or_404(Book, id=book_id)
        for attr, value in data.dict().items():
            setattr(book, attr, value)
        book.save()
        return book
    except Exception as e:
        raise HttpError(400, f"Error updating book: {str(e)}")

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    try:
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return {"success": True}
    except Exception as e:
        raise HttpError(400, f"Error deleting book: {str(e)}")

@api.get("/books", response=list[BookSchema])
def list_books(request):
    try:
        return Book.objects.all()
    except Exception as e:
        raise HttpError(400, f"Error listing books: {str(e)}")

@api.post("/borrow", response=BorrowSchema)
def borrow_book(request, data: BorrowCreateSchema):
    try:
        user = get_object_or_404(User, id=data.user_id)
        book = get_object_or_404(Book, id=data.book_id)
        if book.is_borrowed:
            raise HttpError(400, "Book is already borrowed")
        borrow = Borrow.objects.create(user=user, book=book)
        book.is_borrowed = True
        book.save()
        return borrow
    except Exception as e:
        raise HttpError(400, f"Error borrowing book: {str(e)}")

@api.post("/return/{borrow_id}", response=BorrowSchema)
def return_book(request, borrow_id: int):
    try:
        borrow = get_object_or_404(Borrow, id=borrow_id, return_date=None)
        borrow.return_date = date.today()
        borrow.book.is_borrowed = False
        borrow.book.save()
        borrow.save()
        return borrow
    except Exception as e:
        raise HttpError(400, f"Error returning book: {str(e)}")
