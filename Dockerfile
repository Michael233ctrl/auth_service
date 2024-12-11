FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR auth_service
COPY requirements.txt src /auth_service/
RUN pip install --no-cache-dir -r requirements.txt