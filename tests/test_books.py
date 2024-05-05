from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.database import storage
from app.database.models.books import Books

TEST_JSON = {
    "title": "test_title",
    "author": "Michael",
    "year": 2024,
    "isbn": "bshb-7324-qgd-3727",
}

UPDATE_JSON = {
    "title": "updated title",
    "author": "updated Michael",
    "year": 2000,
    "isbn": "bshb-7324-qgd-3727",
}

BOOK_ID = []


client = TestClient(app)


def test_retrieve_all_books():
    """test for retrieve all books"""
    response = client.get("/api/v1/books")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [book.to_dict() for book in storage.all(Books)]


def test_create_book():
    """test for create a new book endpoint"""
    response = client.post("api/v1/books", json=TEST_JSON)
    assert response.status_code == status.HTTP_201_CREATED
    book_data = response.json()
    BOOK_ID.append(book_data.get("id"))
    assert book_data.get("title") == "test_title"
    assert book_data.get("author") == "Michael"
    assert book_data.get("year") == 2024
    assert book_data.get("isbn") == "bshb-7324-qgd-3727"
    assert "id" in book_data


def test_retrieve_a_book_failed():
    """test for retrieve a book end point on failure"""
    book_id = "this-is-an-invalid-id"
    response = client.get(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Book Not Found"}


def test_retrieve_a_book_success():
    """test for retrieve a book end point on success"""
    book_id = BOOK_ID[0]
    response = client.get(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_200_OK
    book = storage.get(Books, book_id)
    assert response.json() == book.to_dict()


def test_update_book_failed():
    """test for update a book end point on failure"""
    book_id = "this-is-an-invalid-id"
    response = client.put(f"api/v1/books/{book_id}", json=UPDATE_JSON)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Book Not Found"}


def test_update_book_success():
    """test for update a book end point on success"""
    book_id = BOOK_ID[0]
    response = client.put(f"api/v1/books/{book_id}", json=UPDATE_JSON)
    assert response.status_code == status.HTTP_200_OK

    book_data = response.json()

    assert book_data.get("title") == "updated title"
    assert book_data.get("author") == "updated Michael"
    assert book_data.get("year") == 2000
    assert book_data.get("isbn") == "bshb-7324-qgd-3727"


def test_delete_book_failed():
    """test for delete a book end point on failure"""
    book_id = "this-is-an-invalid-id"
    response = client.delete(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Book Not Found"}


def test_delete_book_success():
    """test for delete book endpoint on success"""
    book_id = BOOK_ID[0]
    response = client.delete(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "book deleted successfully"}

    response = client.get(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Book Not Found"}
