### Build
docker build --file Dockerfile --tag controlpanel .

### Run
docker run \
  --rm \
  --name controlpanel-migrate \
  --network contrib_default \
  --network-alias controlpanel \
  --env DB_HOST=postgres \
  --env DB_PORT=5432 \
  --env DB_NAME=controlpanel \
  --env DB_USER=controlpanel \
  --env DB_PASSWORD=controlpanel \
  --env ENABLE_DB_SSL=false \
  --env MODE=migrate \
  controlpanel

docker run \
  --rm \
  --name controlpanel \
  --network contrib_default \
  --network-alias controlpanel \
  --env DB_HOST=postgres \
  --env DB_PORT=5432 \
  --env DB_NAME=controlpanel \
  --env DB_USER=controlpanel \
  --env DB_PASSWORD=controlpanel \
  --env ENABLE_DB_SSL=false \
  --env MODE=run \
  --publish 8000:8000 \
  controlpanel
