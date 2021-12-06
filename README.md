# messenger

Install postgresql https://www.postgresql.org/download/

Create db and user:

`CREATE DATABASE messenger;`

`CREATE USER messenger_user WITH PASSWORD '12345678';`

`GRANT ALL PRIVILEGES ON DATABASE messenger TO messenger_user;`

Upgrade your pip version `python3 -m pip install --upgrade --user pip`

Create and activate virtual environment

Install poetry `pip3 install -r requirements.txt`

Run server `python3 server.py`

To see docs open in browser http://127.0.0.1:8000/docs

Create migration `alembic revision --autogenerate -m 'some commit text'`

DB upgrade `alembic upgrade head`