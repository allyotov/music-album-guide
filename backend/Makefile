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
	poetry run python manage.py runserver localhost:8000

populate.db:
	poetry run python manage.py populate_db

shell:
	poetry run python manage.py shell

lint.core:
	@flake8 core/
	@mypy core/

lint.backend:
	@flake8 backend/
	@mypy backend/