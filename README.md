# Vehicle Management System (Django)

## 📌 Project Overview
The **Vehicle Management System** is a Django-based web application that allows users to manage vehicle records with role-based access control. The system supports CRUD operations on vehicle data and enforces different permissions for Super Admin, Admin, and User roles.

This project is built following **OOP principles**, Django best practices, and basic security considerations.

---

## 🚀 Features

### 🔐 User Roles & Permissions
- **Super Admin**
  - Create, Read, Update, Delete vehicles
  - Manage users and roles
- **Admin**
  - View and Edit vehicle details
- **User**
  - View vehicle details only

### 🚗 Vehicle Management (CRUD)
Each vehicle has the following fields:
- Vehicle Number (Alphanumeric)
- Vehicle Type (Two / Three / Four Wheeler)
- Vehicle Model
- Vehicle Description

### 🛡 Security Features
- **XSS Protection**
  - Django template auto-escaping
  - Input validation using Django Forms
- **IP Filtering**
  - Custom Django middleware to allow/block IP addresses

---

## 🧱 Technology Stack
- **Backend**: Python, Django
- **Database**: SQLite
- **Frontend**: HTML, CSS (Django Templates)
- **Authentication**: Django Auth System
- **Middleware**: Custom IP filtering middleware

---

## 📂 Project Structure
```
vehicle_management/
│
├── manage.py
├── requirements.txt
├── vehicle_management/
│   ├── settings.py
│   ├── urls.py
│   ├── middleware.py
│
├── vehicles/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│
├── templates/
│   ├── base.html
│   ├── vehicle_list.html
│   ├── vehicle_form.html
│
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd vehicle_management
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server
```bash
python manage.py runserver
```

Access the application at:
```
http://127.0.0.1:8000/
```

---

## 🧪 OOP & Design Approach
- Business logic separated into **models, views, and forms**
- Class-based structure for better maintainability
- Role-based access control implemented using Django’s LoginRequiredMixin and PermissionRequiredMixin with model-level permissions for Create, View, Update, and Delete operations.

---

## 📄 requirements.txt
```
Django>=4.0
```

---

## 👤 Author
**Sunilkumar Kahar**  
📧 sunil1998kahar@gmail.com  
📱 +91-9082512576
