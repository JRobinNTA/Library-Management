# Ragam'25 Library Management System

## Project Overview
This is a Django-based Library Management System with RESTful API endpoints for managing books and users, featuring JWT authentication.

## Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ragam-library-management.git
cd ragam-library-management
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints
- `POST /api/register/`: User Registration
  - Request Body:
    ```json
    {
        "username": "johndoe",
        "email": "john@example.com", 
        "password": "securepassword",
        "membership_type": "REGULAR"
    }
    ```

- `POST /api/token/`: Get JWT Token
  - Request Body:
    ```json
    {
        "username": "johndoe",
        "password": "securepassword"
    }
    ```
  - Response: Access and Refresh tokens

- `POST /api/token/refresh/`: Refresh JWT Token

### Book Endpoints
- `GET /api/books/`: List all books
  - Requires Authentication

- `POST /api/books/`: Add a new book 
  - Admin/Staff Access Only
  - Request Body:
    ```json
    {
        "title": "Django for Beginners",
        "author": "William Vincent",
        "published_year": 2020,
        "genre": "SCIENCE",
        "available_copies": 5
    }
    ```

- `GET /api/books/{id}/`: Get book details
- `PUT /api/books/{id}/`: Update book details (Admin only)
- `DELETE /api/books/{id}/`: Delete a book (Admin only)

### User Endpoints
- `GET /api/users/`: List all users
- `GET /api/users/{id}/`: Get user details
- `PUT /api/users/{id}/`: Update user information

## Deployment Checklist
- Set `DEBUG = False` in production
- Use environment variables for sensitive information
- Configure a production-ready database (PostgreSQL recommended)
- Set up proper CORS and security settings

## Possible Genre Choices
- FICTION
- NON_FICTION
- SCIENCE
- HISTORY
- OTHER

## Membership Types
- REGULAR
- PREMIUM

## Authentication
- Uses JWT (JSON Web Tokens)
- Token must be included in Authorization header:
  ```
  Authorization: Bearer <your_access_token>
  ```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

