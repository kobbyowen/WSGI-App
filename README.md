# WSGI-App
A basic WSGI application from scratch, served using apache server. WSGI is what high-level web frameworks like Flask, Django and FastAPI are built on, thus you could say, this is how to build your own web framework from scratch.

## Requirements
Docker

## Setting Up The Project
Change directory to project

```
docker -build -t test/wsgi-app .
docker run -d -p 8000:80 test/wsgi-app
```

NB : You can change container name and port
