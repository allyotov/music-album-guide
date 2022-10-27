#!make
include ../.local.env
export


makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

create.superuser:
	poetry run python manage.py createsuperuser --noinput --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}

runserver:
	poetry run python manage.py runserver localhost:7000

shell:
	poetry run python manage.py shell

lint.core:
	@flake8 core