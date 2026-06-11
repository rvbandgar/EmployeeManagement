# Employee Management System

A Django-based web application for managing employee records with full CRUD (Create, Read, Update, Delete) operations.

## Features

- Add new employees with details like name, designation, skills, and experience
- View list of all employees
- Edit existing employee information
- Delete employee records
- Employee directory management
- Skills and educational qualification tracking
- Django signals integration for post-save operations

## Technologies Used

- **Backend**: Django 5.0.3
- **Database**: PostgreSQL (configured) / SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Additional**: Django Signals

## Prerequisites

- Python 3.10 or higher
- PostgreSQL (for production) or SQLite (for development)
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd project1
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django psycopg2-binary mysqlclient
   ```

4. **Navigate to the project directory:**
   ```bash
   cd tutorial
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000`

## Database Configuration

The project is configured to use PostgreSQL by default. To use SQLite for development:

In `tutorial/settings.py`, comment out the PostgreSQL DATABASES setting and uncomment the SQLite one.

## Project Structure

```
tutorial/
├── app/                    # Main Django app
│   ├── models.py          # Database models (Employee, EmployeeDirectory, etc.)
│   ├── views.py           # View functions for CRUD operations
│   ├── urls.py            # URL patterns
│   ├── signals.py         # Django signals
│   └── templates/         # HTML templates
├── tutorial/              # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── db.sqlite3             # SQLite database (development)
├── manage.py              # Django management script
└── static/                # Static files (CSS, JS, images)
```

## Usage

- **Home Page**: Navigate to the base URL to access the application
- **Add Employee**: Use the form to add new employee records
- **View Employees**: Browse the list of employees
- **Edit/Delete**: Modify or remove employee information

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.