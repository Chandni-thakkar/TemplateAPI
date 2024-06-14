# Django DRF and PostgreSQL Template Management API

This project provides APIs for managing templates and their associated users using Django REST Framework (DRF) and PostgreSQL.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Chandni-thakkar/TemplateAPI.git
    cd django-template-api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL:**

    - Install PostgreSQL if it is not already installed.
    - Create a database and user for the project.

5. **Update the database settings in `settings.py`:**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## API Endpoints

- **Create a Template:**
    ```sh
    POST /templates/
    ```

    ```json
    {
        "template_version": 1,
        "channel": "EMAIL",
        "users": [
            {
                "email": "p.bhavin29@gmail.com",
                "email_type": "PRIMARY",
                "total_visitors": 12,
                "visit_link": "google",
                "organization_name": "Google",
                "visit_request_number": "VST-23434324",
                "visit_cancelled_stage_reason": "",
                "visit_start_time": "12:12",
                "recipient_name": "my name",
                "type_of_visit": "General",
                "visit_end_time": "15:00 pm",
                "visit_start_date": "12-jan-2015"
            }
        ]
    }
    ```

- **Get All Templates:**
    ```sh
    GET /templates/
    ```

- **Get Template by ID:**
    ```sh
    GET /templates/{id}/
    ```

- **Update a Template:**
    ```sh
    PUT /templates/{id}/
    ```

- **Delete a Template:**
    ```sh
    DELETE /templates/{id}/
    ```


