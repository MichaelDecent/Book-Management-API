from fastapi import APIRouter

from app.api.v1.routes.books import router as book_router

router = APIRouter()

router.include_router(book_router, prefix="/books", tags=["books"])
