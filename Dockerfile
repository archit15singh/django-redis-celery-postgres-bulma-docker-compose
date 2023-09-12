FROM python:3.9.6-slim-buster

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./sales_email_generator /app

WORKDIR /app

RUN echo '#!/bin/bash' > /worker.sh && \
    echo 'celery -A sales_email_generator worker -l error' >> /worker.sh && \
    chmod +x /worker.sh

RUN echo '#!/bin/bash' > /entry.sh && \
    echo 'python manage.py migrate --no-input' >> /entry.sh && \
    echo 'python manage.py wait_for_db' >> /entry.sh && \
    echo 'python manage.py prepare_db' >> /entry.sh && \
    echo 'python manage.py collectstatic --no-input' >> /entry.sh && \
    echo 'gunicorn sales_email_generator.wsgi:application --bind 0.0.0.0:8000' >> /entry.sh && \
    chmod +x /entry.sh
