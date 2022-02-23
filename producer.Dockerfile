FROM python:3

ENV PYTHONBUFFERED 1

COPY producer/requirements.txt .
RUN pip install -r requirements.txt

ADD ./producer .