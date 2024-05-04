FROM python:3.9-slim-buster

WORKDIR /book-api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends sqlite3 libsqlite3-dev && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /book-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /book-api/requirements.txt

COPY . /book-api/

# Set up SQLite database
RUN mkdir -p /sqlite_data
RUN python -c "import sqlite3; conn = sqlite3.connect('/sqlite_data/book.db'); conn.close()"

VOLUME /sqlite_data

CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"]