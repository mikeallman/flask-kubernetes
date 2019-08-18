FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY openapi_server /usr/src/app/openapi_server

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "openapi_server.app:application"]