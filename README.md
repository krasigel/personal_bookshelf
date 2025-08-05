# My Personal Bookshelf

## I. General Information

**Project Name:** My Personal Bookshelf  
**Type:** Django Web Application  
**Goal:** Allows users to create personal bookshelves, add books, rate and review them, and read published articles from admins or moderators.

---

## II. Main Functionality

### 1. User Registration & Authentication
- **Custom registration form** with validation:
  - Must be **18+ years old**
  - Required **unique email**
  - Matching passwords
- Optional **avatar upload**
- Custom **login/logout** views

### 2. User Profile
- Displays personal data:
  - Avatar
  - Username, names, age, email, favorite genres
- Options to **edit** and **delete** the profile

### 3. Bookshelf Features
- Every user has a personal bookshelf (“My Bookshelf”)
- Users can:
  - Add books with cover image, genre, review, and recommendation status
  - Edit and delete their books
  - Rate books (1–5 stars) and view **average ratings**
  - View other users’ bookshelves

### 4. News Section
- News page displays only **published articles** (`/news/`)
- Each article includes:
  - Title, content, image, author, date
- Detailed article view available

### 5. All Bookshelves Page
- Public view of all users and their bookshelves
- Can browse and view other users’ bookshelves
- **Search** for a book title or author (public access)

---

## III. Admin and Moderator Area
- **Superuser** can manage all models via Django Admin.
- **Moderator group** with limited permissions:
  - Can add/edit/delete articles and books
  - Can change or delete readers
  - Cannot assign permissions or create superusers

---

## IV. Project Structure
- **Apps:**
  - `reader` – user registration, login, profile
  - `bookshelf` – books and bookshelf logic
  - `common` – homepage, news articles
- **Technologies:**
  - Django 5.x
  - Python 3.11
  - PostgreSQL (with psycopg2)
  - Pillow (for image handling)
  - python-decouple (for environment variables)
  - HTML, CSS (via static files)

---

## V. Validators
- Custom validator for image extensions (`.jpg`, `.jpeg`, `.png`)
- Age validator – minimum age 18
- Validation for matching passwords and unique email

---

## VI. Testing
Manual testing was performed for:
- Registration (with and without avatar)
- Book creation, editing, deletion
- Star rating system
- Profile editing and deletion
- Article visibility logic
- Book/author search

---

## VII. Project Setup

### 1. Clone the repository

git clone https://github.com/krasigel/personal_bookshelf.git
cd personal_bookshelf

### 2. Create and activate a virtual environment

python -m venv .venv

source .venv/bin/activate     # On macOS/Linux

.venv\Scripts\activate        # On Windows

---

### 3. Install dependencies

pip install -r requirements.txt

---
### 4. Configure the database

Make sure PostgreSQL is installed and running.
Create a database:

CREATE DATABASE personal_bookshelf;

Update DATABASES in settings.py with your DB credentials.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

---

### 5. Apply migrations

python manage.py makemigrations
python manage.py migrate

---
### 6. Create a superuser

python manage.py createsuperuser

---

### 7.Run the server

python manage.py runserver

---

## VIII. GitHub Repository
https://github.com/krasigel/personal_bookshelf\



