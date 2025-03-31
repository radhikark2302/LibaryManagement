# Library Management System

## Overview
The **Library Management System** is a simple Django-based application that allows users to borrow and return books. It manages book records, user borrowing history, and facilitates book tracking.

## Features
- User authentication using Django's built-in `User` model.
- Book management (title, author, published date, availability status).
- Borrowing system to track book lending and returns.

## Technologies Used
- **Django** (Backend Framework)
- **SQLite** (Default Database for Django)
- **Python** (Programming Language)

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/library-management.git
   cd library-management
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Panel Access)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Admin Panel**
   Open `http://127.0.0.1:8000/admin` in your browser and log in with the superuser credentials.

## Usage
- Admins can add and manage books through the Django Admin Panel.
- Users can borrow and return books based on availability.

## API Endpoints (If Implemented)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books |
| POST | `/books/add/` | Add a new book |
| POST | `/borrow/` | Borrow a book |
| POST | `/return/` | Return a borrowed book |

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact
For any queries, reach out to:
- **Radhika**: [radhika.ind2302@gmail.com]
- **GitHub**: [https://github.com/radhikark2302]

