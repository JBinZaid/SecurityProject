## Secure Web Application Project ##

This project is a secure web application built with Flask. It demonstrates the detection and mitigation of common web security vulnerabilities such as SQL Injection, weak password storage, XSS, improper access control, and insecure data transmission.

## Features ##

- User registration and login
- Role-based access control (admin and regular users)
- Password hashing with bcrypt
- Admin panel accessible only to admin users
- Secure session and data transmission
- SQL injection mitigation using SQLAlchemy ORM
- XSS mitigation via input sanitization and template escaping


## Installation & Setup ##

1. install the dependencies:
    pip install -r requirements.txt
2. run the application:
    python run.py
3. access the app at:
    https://127.0.0.1:5000 or the given url in the terminal


to promote a user to admin, the the promote_admin.py script:
    python promote_admin.py

