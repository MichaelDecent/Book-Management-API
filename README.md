# Book Management API

This project is a simple CRUD (Create, Read, Update, Delete) application built with FastAPI and SQLAlchemy. It provides a RESTful API for managing a database of books.

## Features

- **Create**: Add a new book to the collection.
- **Read**: Retrieve information about one or all books.
- **Update**: Modify information about an existing book.
- **Delete**: Remove a book from the collection.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **SQLAlchemy**: A Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Swagger**: Interactive documentation for the API endpoints.
- **Docker**: Containerization for easy deployment and distribution.

## Data Model

Each book in the database has the following attributes:

- `id` (integer, auto-generated): Unique identifier for the book.
- `title` (string): Title of the book.
- `author` (string): Author of the book.
- `year` (integer): Year of publication.
- `isbn` (string): International Standard Book Number.

## API Endpoints

- `GET /books`: Retrieve a list of all books.
- `GET /books/{id}`: Retrieve information about a specific book.
- `POST /books`: Add a new book to the collection.
- `PUT /books/{id}`: Update information about an existing book.
- `DELETE /books/{id}`: Delete a book from the collection.

## Input Validation

- Required fields (`title`, `author`, `year`, `isbn`) must be provided when creating or updating a book.
- Input types and formats are validated (e.g., `year` must be an integer, `isbn` must be a string).

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Docker (optional)

### Installation

1. Clone the repository:
    - `https://github.com/MichaelDecent/Book-Management-API.git`
      
2. Navigate to the project directory:
    - `cd Book-Management-API`
      
3. Create a virtual environment and activate it:   
  - `python -m venv dev-env`
  - `source dev-env/bin/activate`  # On Windows, use `dev-env\Scripts\activate`
    
4. Install the required dependencies:

  - `pip install -r requirements.txt`


### Running the Application

1. Start the development server:

  - `uvicorn main:app --reload`


2. Open your web browser and go to `http://localhost:8000/docs` to access the Swagger documentation and interact with the API.

### Running with Docker

1. Build the Docker image:

 - `make build` 


2. Run the Docker container:

 - `make run`


3. Open your web browser and go to `http://localhost:8000/docs` to access the Swagger documentation and interact with the API.


4. Stop the Docker container:

 - `make stop`

## Testing

1. Run the unit tests with the following command:

  - `pytest`


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.








