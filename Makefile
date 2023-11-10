build-static:
	mkdir -p static/govuk-frontend/govuk/
	cp -R node_modules/govuk-frontend/govuk/assets/ static/govuk-frontend/govuk/assets/
	npm run css


build-js:
	mkdir -p static/js/
	cp node_modules/govuk-frontend/govuk/all.js static/js/govuk.js
