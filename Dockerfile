# 
FROM python:3.9-slim-buster

# 
WORKDIR /book-api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# 
COPY ./requirements.txt /book-api/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /book-api/requirements.txt

# 
COPY . /book-api/

# 
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]