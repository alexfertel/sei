FROM python:alpine

RUN pip install spacy && python -m spacy download en_core_web_sm

VOLUME ["dataset"]

COPY src/ /app

WORKDIR /app