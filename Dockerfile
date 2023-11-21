FROM node:18-alpine AS jsdep
COPY package.json package-lock.json ./
RUN npm install

COPY controlpanel controlpanel
RUN mkdir -p static/assets/fonts
RUN mkdir -p static/assets/images
COPY node_modules/govuk-frontend/govuk/assets/fonts/. static/assets/fonts
COPY node_modules/govuk-frontend/govuk/assets/images/. static/assets/images
RUN npm run css

FROM python:3.11-bullseye AS base

ENV DJANGO_SETTINGS_MODULE="controlpanel.settings"

# create a user to run as
RUN addgroup -gid 1000 controlpanel && \
  adduser -uid 1000 --gid 1000 controlpanel

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        libcurl4-gnutls-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/controlpanel

RUN pip install -U pip

COPY requirements.txt requirements.dev.txt manage.py ./
RUN pip install -U --no-cache-dir pip
RUN pip install -r requirements.txt

USER controlpanel
COPY controlpanel controlpanel
COPY tests tests

RUN mkdir -p static/assets/fonts
RUN mkdir -p static/assets/images
RUN mkdir -p static/assets/js

# install javascript dependencies
COPY --from=jsdep static/app.css static/
COPY --from=jsdep node_modules/govuk-frontend/govuk/assets/fonts/. static/assets/fonts
COPY --from=jsdep node_modules/govuk-frontend/govuk/assets/images/. static/assets/images
COPY --from=jsdep node_modules/govuk-frontend/govuk/all.js static/assets/js/govuk.js

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "controlpanel.asgi:application"]
