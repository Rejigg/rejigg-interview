# Install all reqirements and run the app
run:
	docker compose run --rm frontend npm install
	docker compose run --rm backend pipenv install
	docker compose up --build

# Make and run migrations
migrate:
	docker compose run --rm backend pipenv run ./manage.py makemigrations
	docker compose run --rm backend pipenv run ./manage.py migrate

# Run the backend shell
shell:
	docker compose run --rm backend pipenv run ./manage.py shell

# Install a python package
# Usage: make backend.install package=<package>
backend.install:
	docker compose run --rm backend pipenv install ${package}
	docker compose build

# Install a javascript package
# Usage: make backend.install package=<package>
frontend.install:
	docker compose run --rm frontend npm i ${package}
	docker compose build
