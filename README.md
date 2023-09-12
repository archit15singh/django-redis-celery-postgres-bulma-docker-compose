example fullstack application using:
1. django (backend)
1. bulma css (frontend)
1. nginx (serving static files and reverse proxy)
1. celery (running background tasks)
1. redis (message broker and queue)
1. docker-compose (packaging and deploying)
1. datatables.js (for showing tables in UI)

# Setup
just run `docker-compose build && docker-compose up -d` and check `docker-compose logs -f`

# Flows
1. submission of form creates a job in the celery worker which can be tracked in the in progress screen.
1. view screen integrated with datatables.js
1. create object form which triggers the creation of a background job

# management commands
1. change record size in settings.py for controlling the fake data creation and population in dev setups
