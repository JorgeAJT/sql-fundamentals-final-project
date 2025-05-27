FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATA_PATH=./data_samples
ENV ENVIRONMENT=production
ENV DB_NAME=users-db
ENV DB_USER=root
ENV DB_HOST=users-db-container
ENV DB_PORT=5432

EXPOSE 8080
CMD ["python", "main.py"]
