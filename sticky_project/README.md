#  Sticky Notes App (Django)

A simple web-based Sticky Notes application built using Django. Users can register, log in, and manage their personal notes with features like color selection, pinning, search, and pagination.

---

##  Features

* User Registration, Login & Logout
* Create, Edit, Delete Notes
* Color Picker for notes 
* Pin important notes 
* Search notes 
* Pagination (10 notes per page)
* Character counter for note content

---

##  Requirements

Make sure you have installed:

* Python (3.10 or higher)
* pip (comes with Python)
* Django

---

##  Installation & Setup

### 1. Clone or Download the Project

```bash
git clone <https://github.com/ItxSaeed/sticky-notes-django>
cd sticky_project
```

---

### 2. Install Django

```bash
pip install django
```

---

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Run the Development Server

```bash
python manage.py runserver
```

---

### 5. Open in Browser

```
http://127.0.0.1:8000/login/
```

---

##  Usage

* Register a new account
* Login using your credentials
* Create and manage your notes
* Use search to find notes
* Pin important notes to top

---

##  Project Structure

```
sticky_project/
│
├── manage.py
├── sticky_project/
│   ├── settings.py
│   ├── urls.py
│
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│       ├── base.html
│       ├── note_list.html
│       ├── note_form.html
│       ├── note_confirm_delete.html
│       ├── login.html
│       ├── register.html
```

---

##  Notes

* Each user can only access their own notes
* Logout requires POST request (handled via form)
* SQLite is used as the default database

---

##  Author

Saeed Ahmed

---

## Final Note

This project demonstrates Django fundamentals including models, forms, authentication, views, templates, and CRUD operations.