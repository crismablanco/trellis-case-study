# Trellis Case Study by Cristian Blanco

[![Django CI](https://github.com/crismablanco/trellis-case-study/actions/workflows/django.yml/badge.svg?branch=development)](https://github.com/crismablanco/trellis-case-study/actions/workflows/django.yml)
[![Python application](https://github.com/crismablanco/trellis-case-study/actions/workflows/python-app.yml/badge.svg?branch=development)](https://github.com/crismablanco/trellis-case-study/actions/workflows/python-app.yml)

#
#### __HOW TO RUN WITH DOCKER__
1. Install `docker compose`
2. Go to project root folder and run `docker-compose build`
3. run `docker-compose up` 

#
#### __HOW TO RUN WITH POETRY__
1. Run `pip install poetry`
2. Go to project root folder and run `poetry install`
3. Run `poetry shell`
4. Run `cd api`
5. Run `python manage.py runserver`
(we are not using the database so we don't need to `migrate`)
#
#### __HOW TO CHECK BLACK, PYLINT AND RUN TESTS__
1. Run `pip install poetry` (if you didn't yet)
2. Go to project root folder and run `poetry install`
3. Run `poetry shell`
4. Run `make build`
(coverage is configured to 90%)
#
#### __HOW TO USE THE ENDPOINTS__
1. Make sure the project is running
2. Open your favorite API client (Postman, Insomnia, ...)
3. GET REQUEST: `127.0.0.1:8000/num_to_english/?number=12345678&and_word=`
4. POST REQUEST: `127.0.0.1:8000/num_to_english/` <br>
with json body: 
<br>
`{
	"number": "12345678",
	"and_word": "and"
}`
