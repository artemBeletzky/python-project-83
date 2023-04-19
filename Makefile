PORT ?= 8000

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

dev:
	poetry run flask --app page_analyzer:app run

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

lint:
	poetry run flake8

test:
	poetry run pytest