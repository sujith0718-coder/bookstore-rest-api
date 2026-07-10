# 📚 Bookstore REST API

A beginner-friendly **Bookstore Management REST API** built with **Python** and **Flask**. This project demonstrates how to create a reusable **Library API** for business logic and expose it through a **REST API** with HTTP endpoints.

## 🚀 Features

* 📖 Get all books
* 🔍 Get a book by ID
* ➕ Add a new book
* 🏠 Home endpoint
* ℹ️ About endpoint
* 🧩 Modular project structure
* 📦 Reusable Python Library API
* 🌐 REST API built with Flask

## 🛠️ Technologies Used

* Python
* Flask
* REST API
* Object-Oriented Programming (OOP)
* JSON
* HTTP (GET & POST)
* Postman

## 📂 Project Structure

```text
bookstore-rest-api/
│── app.py
│── bookstore.py
│── requirements.txt
└── README.md
```

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/bookstore-rest-api.git
```

Navigate to the project:

```bash
cd bookstore-rest-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

## 📌 API Endpoints

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/`                | Home                  |
| GET    | `/books`           | Retrieve all books    |
| GET    | `/books/<book_id>` | Retrieve a book by ID |
| POST   | `/books`           | Add a new book        |
| GET    | `/about`           | About the project     |

### Example POST Request

**Endpoint**

```
POST /books
```

**Request Body**

```json
{
    "title": "Clean Code",
    "author": "Robert C. Martin"
}
```

## 💡 Learning Outcomes

Through this project, I gained practical experience with:

* Designing a simple REST API using Flask
* Creating a reusable Python Library API
* Applying Object-Oriented Programming (OOP)
* Organizing code using a modular architecture
* Handling JSON requests and responses
* Working with HTTP methods (GET & POST)
* Using HTTP status codes
* Testing APIs with Postman

## 🚀 Future Improvements

* Add PUT and DELETE endpoints
* Integrate SQLite database
* Implement input validation
* Add authentication
* Deploy the API

## 👨‍💻 Author(Sujith E)

Developed as part of my backend development learning journey using Python and Flask.
