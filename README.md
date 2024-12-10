# Auth Service

The `auth_service` is a microservice responsible for handling user authentication, authorization, and role-based access control (RBAC) in the real-time collaboration backend API. It uses FastAPI for the API implementation and MongoDB for data storage.

---

## Features

- **User Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- **Role-Based Access Control (RBAC)**: Assign roles to users (e.g., admin, editor, viewer) and enforce permissions.
- **User Management**: API endpoints for user registration, login, and profile management.
- **Password Security**: Hashing and salting of passwords using `bcrypt`.

---

## Technologies Used

- **FastAPI**: For building a high-performance Python API.
- **MongoDB**: For storing user data and roles.
- **Pydantic**: For data validation and serialization.
- **bcrypt**: For secure password hashing.

---