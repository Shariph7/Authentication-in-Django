# Authentication System in Django

This is a Django-based Authentication System that allows users to register, log in, and manage their accounts. The project includes features such as user registration, login, logout, password reset, and profile management.

## Features

- **User Registration**: Allows users to create an account with basic validation (username, email, password).
- **Login/Logout**: Secure user login/logout functionality.
- **Password Reset**: Enables users to reset their passwords through email.
- **User Profile Management**: Users can update their profiles and change personal information.
- **User Authentication**: Built-in Django authentication system (using `django.contrib.auth`).
- **Home App**: A basic landing page or dashboard after login.

## Project Structure

Authentication/
├── .gitignore             # Git ignore file for Python/Django related files
├── manage.py              # Django's command-line utility
├── Authentication/        # Core project folder with settings
│   ├── __init__.py        # Marks this directory as a Python package
│   ├── asgi.py            # ASGI configuration for asynchronous support
│   ├── settings.py        # Project settings including Authentication settings
│   ├── urls.py            # Project-level URL routing
│   └── wsgi.py            # WSGI configuration for production environments
├── Home/                  # Home app folder with dashboard/landing page
│   ├── __init__.py        # Marks this directory as a Python package
│   ├── admin.py           # Admin panel configuration for the Home app
│   ├── apps.py            # App configuration for Home
│   ├── models.py          # Database models for the Home app
│   ├── tests.py           # Tests for the Home app
│   ├── views.py           # Views for the Home app
│   ├── migrations/        # Database migrations for the Home app
── templates/              # HTML templates for the Home app (e.g., landing page)


## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Shariph7/Authentication-in-Django.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Authentication
    ```

3. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:

    - On macOS/Linux:
    
      ```bash
      source venv/bin/activate
      ```

    - On Windows:
    
      ```bash
      .\venv\Scripts\activate
      ```

5. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser for the admin panel**:

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    Your app will now be available at `http://127.0.0.1:8000/`.

## How to Use

### User Registration

- Go to `/register/` to create a new user account.
- The registration form will ask for a username, password. The system will ensure that the passwords match and are strong enough.
- Upon successful registration, the user will be logged in automatically and redirected to the home/dashboard page.

### User Login/Logout

- Go to `/login/` to log in using your credentials.
- After logging in, users will be redirected to their dashboard or home page.
- You can log out by clicking the logout button, which will redirect to the home page.

## Customizing the Authentication System

This system is built using Django's built-in authentication system (`django.contrib.auth`). You can extend the user model by creating a custom user model if needed by modifying `authentication/models.py`. Additionally, you can customize the forms and views for user registration, login, and profile management.

### Settings to Change in `settings.py`

- **Authentication Backends**: You can define multiple authentication backends in `settings.py` if you're using social authentication or other methods.

## Running Tests

This project includes basic unit tests for authentication functionality.

To run tests:

```bash
python manage.py test
## Thank You ¬ By Shariph Thapa Magar