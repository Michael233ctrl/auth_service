FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR authenticator
COPY requirements.txt prestart.sh src /authenticator/
RUN pip install --no-cache-dir -r requirements.txt