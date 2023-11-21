FROM public.ecr.aws/docker/library/node:20.9.0 AS build-node

COPY package.json package-lock.json ./
COPY controlpanel/interfaces/web/static/app.scss ./controlpanel/interfaces/web/static/app.scss

RUN npm install \
    && npm run css

FROM public.ecr.aws/docker/library/python:3.11-alpine3.18 AS final

WORKDIR /controlpanel

COPY --from=build-node static/app.css static/app.css

COPY requirements.txt ./

RUN pip install --requirement requirements.txt
