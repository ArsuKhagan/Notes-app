# 📝 Notes App

A simple full-stack notes application built with FastAPI, PostgreSQL, and Docker.

## 🚀 Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Infrastructure:** Docker, Docker Compose

## ✨ Features

- Create notes with a title and content
- View all notes sorted by date
- Delete notes
- Data persists in PostgreSQL

## 📦 Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Run the app

```bash
git clone https://github.com/your-username/notes-app.git
cd notes-app
docker compose up --build
```

Open your browser at **http://localhost:8000**

### Stop the app

```bash
docker compose down
```

## 📁 Project Structure

```
notes-app/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── models.py        # Database models
│   ├── database.py      # PostgreSQL connection
│   └── templates/
│       └── index.html   # Frontend UI
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with all notes |
| POST | `/notes` | Create a new note |
| POST | `/notes/{id}/delete` | Delete a note |
