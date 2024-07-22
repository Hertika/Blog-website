# Django Blog Application

## Introduction
A full-featured blog application created using Django. This application allows users to create, read, update, and delete blog posts. It includes user authentication and authorization to manage user accounts and permissions.

## Features
- Create, read, update, and delete blog posts
- User authentication and authorization
- Manage user accounts and permissions

## Technologies Used
- Django
- HTML/CSS


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Hertika/Blog-website.git
    cd Blog-website
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Access the application:
    Open your web browser and go to `http://127.0.0.1:8000`.

2. Admin Actions:
    - Log in to the admin panel at `http://127.0.0.1:8000/admin`.
    - Manage blog posts, user accounts, and permissions.

3. User Actions:
    - Sign up, log in, and create blog posts.
    - Edit or delete your blog posts.




