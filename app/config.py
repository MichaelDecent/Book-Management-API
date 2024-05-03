from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "BOOK MANAGEMENT API"
VERSION = "1.0.0"
API_PREFIX = "/api/v1"

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

DB_NAME = config("DB_NAME", cast=Secret)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=f"sqlite:////sqlite_data/{DB_NAME}",
)
