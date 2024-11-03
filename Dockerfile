FROM python:3.10.9
RUN apt update && apt-get install default-libmysqlclient-dev gcc netcat -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY . .

RUN chmod +x entrypoint.sh

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 5000