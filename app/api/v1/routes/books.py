from fastapi import APIRouter, status, HTTPException
from typing import List, Dict
from app.database.models.books import Books, BooksIn, BooksOut
from app.database import storage

router = APIRouter()


def get_book_or_raise_exception(book_id: str) -> Books:
    book = storage.get(Books, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Book ID"
        )
    return book


@router.get("/", status_code=status.HTTP_200_OK)
async def retrieve_all_books() -> List[BooksOut]:
    """Retrieve a list of all books."""
    return storage.all(Books).values()


@router.get("/{book_id}/", response_model=BooksOut, status_code=status.HTTP_200_OK)
async def retrieve_a_book(book_id: str) -> BooksOut:
    """Retrieve information about a specific book"""
    return get_book_or_raise_exception(book_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BooksIn) -> BooksOut:
    """Add a new book to the collection"""
    new_book = Books(**book_data.model_dump())
    new_book.save()
    return new_book


@router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: str, book_data: BooksIn):
    """Update information about an existing book"""
    book = get_book_or_raise_exception(book_id)
    for key, value in book_data.model_dump().items():
        if key is not None:
            setattr(book, key, value)
    storage.save()
    return book


@router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: str) -> Dict:
    """Delete a book from the collection"""
    book = get_book_or_raise_exception(book_id)
    storage.delete(book)
    storage.save()
    return {"message": "book deleted successfully"}
