all:
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
