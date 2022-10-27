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

rebuild.backend:
	docker-compose up -d --no-deps --build backend

volumes.down:
	docker-compose down -v

populate.db:
	docker-compose exec backend poetry run python manage.py populate_db
