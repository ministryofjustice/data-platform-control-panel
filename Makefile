#!make

REPOSITORY ?= controlpanel
IMAGE_TAG ?= local
REGISTRY ?= 593291632749.dkr.ecr.eu-west-1.amazonaws.com
export

build:
	make build-static
	make build-js

build-static:
	mkdir -p static/assets/fonts
	mkdir -p static/assets/images
	cp -R node_modules/govuk-frontend/govuk/assets/fonts/. static/assets/fonts
	cp -R node_modules/govuk-frontend/govuk/assets/images/. static/assets/images
	npm run css

build-js:
	mkdir -p static/assets/js
	cp node_modules/govuk-frontend/govuk/all.js static/assets/js/govuk.js

build-image:
	docker build -t ${REGISTRY}/${REPOSITORY}:${IMAGE_TAG} . --load

db-migrate:
	python manage.py migrate

db-drop:
	python manage.py reset_db

serve:
	python manage.py runserver

test:
	@echo
	@echo "> Running Python Tests (In Docker)..."
	@docker-compose run --rm interfaces sh -c "pytest tests --color=yes"

clean:
	@docker-compose down --remove-orphans
