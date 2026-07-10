# 📚 Bookstore REST API

A simple **Bookstore Management REST API** built with **Python** and **Flask** to demonstrate REST API fundamentals, modular project architecture, and Object-Oriented Programming (OOP).

The project separates the business logic into a reusable **Library API** (`bookstore.py`) while exposing HTTP endpoints through a **Flask REST API** (`app.py`).

---

## 🚀 Features

* 📖 Get all books
* 🔍 Get a book by ID
* ➕ Add a new book
* 🏠 Home endpoint
* ℹ️ About endpoint
* 🧩 Modular architecture
* 📦 Reusable Python Library API
* 🌐 Flask REST API
* ✅ Tested using Postman

---

## 🛠️ Tech Stack

* Python
* Flask
* REST API
* Object-Oriented Programming (OOP)
* JSON
* HTTP (GET & POST)
* Postman

---

## 📂 Project Structure

```text
bookstore-rest-api/
│── app.py
│── bookstore.py
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sujith0718-coder/bookstore-rest-api.git
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

The application will start at:

```text
http://127.0.0.1:5000
```

---

## 📌 API Endpoints

| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| GET    | `/`           | Home                  |
| GET    | `/books`      | Retrieve all books    |
| GET    | `/books/<id>` | Retrieve a book by ID |
| POST   | `/books`      | Add a new book        |
| GET    | `/about`      | About the project     |

---

## 📥 Example POST Request

**Endpoint**

```http
POST /books
```

**Request Body**

```json
{
    "title": "Clean Code",
    "author": "Robert C. Martin"
}
```

**Response**

```json
{
    "id": 3,
    "title": "Clean Code",
    "author": "Robert C. Martin"
}
```

---

## 🎯 Learning Outcomes

This project helped me understand:

* Building REST APIs with Flask
* Designing a reusable Python Library API
* Applying Object-Oriented Programming (OOP)
* Modular application architecture
* HTTP methods (GET & POST)
* JSON request and response handling
* Dynamic routes using URL parameters
* HTTP status codes
* API testing with Postman

---

## 🔮 Future Improvements

* ✏️ PUT endpoint
* ❌ DELETE endpoint
* 🗄️ SQLite database integration
* ✅ Input validation
* 🔐 Authentication
* ☁️ Cloud deployment

---

## 👨‍💻 Author

**Sujith**

GitHub: https://github.com/sujith0718-coder

If you found this project helpful, consider giving it a ⭐.
