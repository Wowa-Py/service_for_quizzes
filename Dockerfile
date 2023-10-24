FROM postgres:latest
ENV POSTGRES_USER=testuser
ENV POSTGRES_PASSWORD=testpassword
ENV POSTGRES_DB=testdb
COPY init.sql /docker-entrypoint-initdb.d/

FROM python:3.8
WORKDIR /web-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

