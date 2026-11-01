# 🚀 My Tracker – Full-Stack Application with FastAPI

A full-stack web application built while learning **FastAPI, Python, REST APIs, Pydantic, SQLAlchemy, and Database Integration**.

This project focuses on understanding how to build high-performance backend applications, develop RESTful APIs, validate data, interact with relational databases, and connect backend services with a frontend application.

## 📌 Project Overview

My Tracker is a hands-on learning project developed to strengthen my backend and full-stack development skills using FastAPI.

Through this project, I explored how to build a server, implement CRUD operations, integrate a database using SQLAlchemy, and manage application data efficiently.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| Pydantic | Data validation |
| SQLAlchemy | Object Relational Mapping (ORM) |
| PostgreSQL / SQL Database | Data persistence |
| HTML, CSS, JavaScript | Frontend development |
| VS Code | Development environment |
| Git & GitHub | Version control |

## ✨ Features & Implementations

- **FastAPI Server Setup:** Created and configured a backend server using FastAPI.
- **REST API Development:** Implemented GET, POST, PUT, and DELETE endpoints.
- **Data Validation:** Used Pydantic models to validate incoming request data.
- **Product Management:** Implemented functionality to fetch all products and retrieve individual products by ID.
- **Database Integration:** Connected the application to a relational database using SQLAlchemy.
- **Database Models:** Created SQLAlchemy models to represent application data.
- **CRUD Operations:** Implemented database operations to create, retrieve, update, and delete records.
- **Dependency Injection:** Used FastAPI dependency injection for database session management.
- **Full-Stack Integration:** Explored connecting the backend APIs with a frontend application.

## 🏗️ Application Architecture

The application follows a basic full-stack architecture:

```text
             Frontend
                 |
                 |
             HTTP Requests
                 |
                 ▼
          FastAPI Backend
                 |
                 ▼
          API Endpoints
       GET | POST | PUT | DELETE
                 |
                 ▼
           Pydantic
          Validation
                 |
                 ▼
           SQLAlchemy
              ORM
                 |
                 ▼
           SQL Database
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ayyeshakhann5-bit/My-Tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd My-Tracker
```

### 3. Create a Virtual Environment

```bash
python3 -m venv myenv
```

### 4. Activate the Virtual Environment

For macOS / Linux:

```bash
source myenv/bin/activate
```

For Windows:

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

Install any additional dependencies required by the project.

### 6. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

*Note: Update `main:app` if your FastAPI application uses a different Python module or application variable.*


## 🔗 REST API Operations

| HTTP Method | Operation | Description |
|---|---|---|
| GET | Read | Retrieve all products |
| GET | Read by ID | Retrieve a specific product |
| POST | Create | Add a new product |
| PUT | Update | Modify existing product details |
| DELETE | Delete | Remove a product |

## 🎯 Key Takeaways

Through this project, I gained practical experience in:

- Understanding FastAPI fundamentals and backend architecture.
- Designing and implementing RESTful APIs.
- Working with HTTP methods and CRUD operations.
- Validating API requests using Pydantic.
- Integrating relational databases using SQLAlchemy.
- Managing database sessions and dependencies.
- Connecting frontend and backend components.

## 👩‍💻 Author

**Ayesha Khan**

Aspiring Software Developer | Python | FastAPI | SQL | Backend Development

---

⭐ If you find this project useful, feel free to explore the repository!
