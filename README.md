# monday.com webhook fastapi example
This repo contains example of integration Monday.com webhook in fastapi python.
In this example if the status of item is change in board this webhook triggers and send email in background task

## Requirements
Python 3.11.4

## Quickstart

**1. Copy example.env to .env**

**2. place SENDGRID_API_KEY, FROM_EMAIL, TO_EMAIL in .env**

**3. create virtual env**
```sh
python -m venv venv
```

**4. install requirements**
```sh
pip install -r requirements.txt
```

**5. Run it**
```sh
uvicorn main:app --reload
```




