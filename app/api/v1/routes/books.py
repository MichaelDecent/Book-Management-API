from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def retrieve_all_books():
    """Retrieve a list of all books."""
    pass


@router.get("/{book_id}/")
async def retrieve_a_book():
    """Retrieve information about a specific book"""
    pass


@router.post("/")
async def create_book():
    """Add a new book to the collection"""
    pass


@router.put("/")
async def update_book():
    """Update information about an existing book"""
    pass


@router.delete("/")
async def delete_book():
    """Delete a book from the collection"""
    pass
