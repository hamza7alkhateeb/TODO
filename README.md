# ToDo Tasks Management

## 📌 About the Project

This project is a simple **ToDo Tasks Management** application built with **Django**.
It allows users to **register**, **login**, and manage their personal tasks.

The main features include:

* **User Authentication**: Login & Register system.
* **Home Page**: Displays a list of tasks for the logged-in user.
* **Task Details Page**: View detailed information about each task.
* **Task Management**: Add, edit, delete, and mark tasks as completed.
* **Contact Page**: A page that allows users to reach out for communication
* **About Page**: A simple page that introduces information about me

Initially, the project was implemented using **Function-Based Views (FBVs)**, and later refactored to use **Class-Based Views (CBVs)** for cleaner and more scalable code.

---

## ⚙️ Tech Stack

* **Python** & **Django**
* **SQLite** (default development database) and **POSTGRESQL**
* **CSS** (for frontend styling)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hamza7alkhateeb/TODO.git
cd TODO
```

### 2. Create & activate virtual environment

```bash
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

---

## 📝 Notes

* You can create a superuser for Django Admin with:

```bash
python manage.py createsuperuser
```

