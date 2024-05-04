IMAGE_NAME=book-api
CONTAINER_NAME=book-api-container

.PHONY: build run stop clean

build:
	sudo docker build -t $(IMAGE_NAME) .

run:
	sudo docker rm -f $(CONTAINER_NAME) || true
	sudo docker run -d --name $(CONTAINER_NAME) -v sqlite_data:/sqlite_data -p 8000:8000 $(IMAGE_NAME)

stop:
	sudo docker stop $(CONTAINER_NAME)

clean:
	sudo docker rm -f $(CONTAINER_NAME)
	sudo docker rmi $(IMAGE_NAME)