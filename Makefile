local.db.install:
	docker-compose -f postgres-local.yml up -d

local.db.down:
	docker-compose -f postgres-local.yml down