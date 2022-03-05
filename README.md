# NexusHub DevOps Assignment

## Setup

1. Clone this repo
2. Create a virtualenv: `virtualenv venv`
3. Active the env: `source venv/bin/activate`
4. run `make install` or `pip install -r requirements.txt`
5. run `make run-dev` or `python manage.py runserver`

## API Endpoints

### hello-world  
URL: `http://127.0.0.1:8000/hello-world/hello`  
Method: `POST`  
Content-Type: `application/json`  
Request Body: (Example): `{"name": "Timothy"}`  
Expected Response: `"Hello, Timothy!"`

### test (Use for testing the hello-word endpoint)  
URL: `http://127.0.0.1:8000/hello-world/hello`  
Method: `GET`  
Expected Response: `"OK"`

