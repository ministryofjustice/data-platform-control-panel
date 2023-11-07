#!/usr/bin/env bash

# Upgrade NPM
npm install --global npm@latest

# Upgrade Pip
pip install --upgrade pip

# Start Postgres
docker-compose --file contrib/docker-compose-postgres.yml up --detach