# Library Management System
A simple flask app to manage users along with mysql service

![Libray Management App - Flask](https://github.com/hamzaavvan/library-management-system/blob/master/ss/ss2.JPG?raw=true)


## Installation

To run the app flawlessly, satisfy the requirements
```bash
$ pip install -r requirements.txt
```

## Set Environment Variables
```bash
$ export FLASK_APP=app.py
$ export FLASk_ENV=development
```

## Start Server
```bash
$ flask run
```

Or run this command 
```bash
$ python -m flask run
```

## Run With Docker
```bash
$ docker compose up --build
```

The Flask app will be available at `http://127.0.0.1:8000`.

The MySQL container initializes the `lms` database from `db/lms.sql` on first start. If you need to reload the SQL dump from scratch, remove the saved MySQL volume first:
```bash
$ docker compose down -v
$ docker compose up --build
```
