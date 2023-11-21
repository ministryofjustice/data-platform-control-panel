FROM public.ecr.aws/docker/library/node:20.9.0 AS build-node

COPY package.json package-lock.json ./
COPY controlpanel/interfaces/web/static/app.scss ./controlpanel/interfaces/web/static/app.scss

RUN npm install \
    && npm run css

FROM public.ecr.aws/docker/library/python:3.11-alpine3.18 AS final

WORKDIR /controlpanel

RUN mkdir --parents static/assets/fonts \
    && mkdir --parents static/assets/images \
    && mkdir --parents static/assets/js

COPY --from=build-node static/app.css static/app.css
COPY --from=build-node node_modules/govuk-frontend/govuk/assets/fonts/. static/assets/fonts
COPY --from=build-node node_modules/govuk-frontend/govuk/assets/images/. static/assets/images
COPY --from=build-node node_modules/govuk-frontend/govuk/all.js static/assets/js/govuk.js
COPY scripts/container/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY requirements.txt manage.py ./
COPY controlpanel controlpanel

RUN pip install --requirement requirements.txt
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["run"]
