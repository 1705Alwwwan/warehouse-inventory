Warehouse Management System

Features
- Product Management
- Supplier Management
- Stock In
- Stock Out
- Stock Report
- Transaction Report

Technology
- Django
- Bootstrap 5
- SQLite
- Docker

Installation

git clone ...

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Docker

docker build -t warehouse .

docker run -p 8000:8000 warehouse