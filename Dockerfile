FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /regal

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mysite .