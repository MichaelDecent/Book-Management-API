from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.database import storage
from app.database.models.books import Books


test_json = {
    "title": "test_title",
    "author": "Michael",
    "year": 2024,
    "isbn": "bshb-7324-qgd-3727",
}

BOOK_ID = []


client = TestClient(app)


def test_retrieve_all_books():
    """test for retrieve all books"""
    response = client.get("/api/v1/books")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == storage.all(Books)


def test_create_book():
    """test for create a new book endpoint"""
    response = client.post("api/v1/books", json=test_json)
    assert response.status_code == status.HTTP_201_CREATED
    book_data = response.json()
    BOOK_ID.append(book_data.get("id"))
    assert book_data.get("title") == "test_title"
    assert book_data.get("author") == "Michael"
    assert book_data.get("year") == 2024
    assert book_data.get("isbn") == "bshb-7324-qgd-3727"
    assert "id" in book_data


def test_delete_book():
    """test for delete book endpoint"""
    book_id = BOOK_ID[0]
    print(book_id)
    response = client.delete(f"api/v1/books/{book_id}")
    assert response.status_code == status.HTTP_201_CREATED


# def test_retrieve_a_book():
#     """"""
#     book_id = "239b21fa-1657-4088-9790-728f8bfcb425"
#     response = client.get(f"/api/v1/books/{book_id}")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == storage.get(Books, book_id)
