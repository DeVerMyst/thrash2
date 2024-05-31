# User Management API

## Overview

This User Management API provides a RESTful interface for managing users in a SQLite database. The API allows clients to perform CRUD operations on user data, including creating new users, retrieving user information, updating user details, and deleting users. The API also includes authentication mechanisms to verify user credentials.


```
API-BDD/
│
├── apidocs/
│   └── openapi.yaml
│
├── project/
│   ├── __init__.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user_routes.py
│   │
│   └── models/
│       ├── __init__.py
│       └── user.py
│
├── .venv
├── db.sqlite
├── .gitignore
├── README.md
├── create_db.py
├── run.py
├── requete_to_test.ipynb
└── requirements.txt
```

## Features

- **Create a user:** Add a new user with an email, name, and password.
- **Get all users:** Retrieve a list of all users.
- **Get a user by ID:** Retrieve the details of a specific user by their ID.
- **Update a user:** Update the information of an existing user.
- **Delete a user:** Remove a user from the database.
- **User authentication:** Verify user credentials during login.

## Setup

### Prerequisites

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/blueprint
    cd blueprint
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    python create_db.py
    ```

5. Run the application:
    ```bash
    python run.py
    ```

The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Get All Users

- **URL:** `/users`
- **Method:** `GET`
- **Description:** Retrieves a list of all users.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "email": "user@example.com",
          "name": "John Doe"
      },
      ...
  ]
