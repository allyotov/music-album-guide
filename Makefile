install:
	docker-compose up -d

down:
	docker-compose down

local.db.install:
	docker-compose -f postgres-local.yml up -d

local.db.down:
	docker-compose -f postgres-local.yml down

postgres.logs:
	docker-compose logs postgres

backend.logs:
	docker-compose logs backend

backend.runserver:
	docker-compose exec backend run python manage.py runserver

frontend.runserver:
	docker-compose exec frontend run python manage.py runserver

rebuild.backend:
	docker-compose up -d --no-deps --build backend

frontend.logs:
	docker-compose logs frontend

rebuild.frontend:
	docker-compose up -d --no-deps --build frontend

volumes.down:
	docker-compose down -v

populate.db:
	docker-compose exec backend poetry run python manage.py populate_db
