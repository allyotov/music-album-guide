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

frontend.logs:
	docker-compose logs frontend

nginx.logs:
	docker-compose logs nginx

restart.nginx:
	docker-compose restart nginx

backend.collectstatic:
	docker-compose exec backend python manage.py collectstatic

frontend.collectstatic:
	docker-compose exec frontend python manage.py collectstatic

rebuild.backend:
	docker-compose up -d --no-deps --build backend

rebuild.frontend:
	docker-compose up -d --no-deps --build frontend

volumes.down:
	docker-compose down -v

populate.db:
	docker-compose exec backend poetry run python manage.py populate_db
