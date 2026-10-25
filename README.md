# Full-Stack Dealership Capstone

Repository: `fullstack-dealership-capstone`  
Project: **Cars Dealership Web Application**

A learning/demo full-stack dealership application using Django, Django REST-style JSON endpoints, SQLite, and a React registration component.

## Features
- Django admin and session login/logout
- JSON registration endpoint
- Dealer list, dealer details, state filtering, and reviews
- Create review endpoint
- Basic sentiment analysis endpoint
- Car makes/models endpoint
- Static About Us and Contact Us pages
- React registration component
- cURL examples for testing

## Run locally (Windows PowerShell)
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/

## API endpoints
- `POST /accounts/login/`
- `POST /accounts/logout/`
- `POST /accounts/register/`
- `GET /api/dealers/`
- `GET /api/dealers/<id>/`
- `GET /api/dealers/<id>/reviews/`
- `GET /api/dealers/state/<state>/`
- `POST /api/dealers/<id>/reviews/create/`
- `GET /api/carmakes/`
- `POST /api/analyze/`

Use real outputs from your local server in assessment answers. Screenshots and deployment evidence must be captured from a real running/deployed app; do not invent them.
