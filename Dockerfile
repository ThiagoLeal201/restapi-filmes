FROM python:3.11.9-alpine3.20

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY wsgi.py .
COPY config.py .
COPY application application

CMD [ "python", "wsgi.py" ]