#!make
include ../.local.env
export

runserver:
	poetry run python manage.py runserver localhost:7000

collectstatic:
	poetry run python manage.py collectstatic

lint.core:
	@flake8 core/
	@mypy core/

lint.frontend:
	@flake8 frontend/
	@mypy frontend/