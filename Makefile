build-static:
	mkdir -p static/govuk-frontend/govuk/
	cp -R node_modules/govuk-frontend/govuk/assets/ static/govuk-frontend/govuk/assets/
	npm run css
