# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install any dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5000

ENV OTEL_SERVICE_NAME="test-app"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://simplest-jaeger-collector.observability.svc.cluster.local:4318"

# Set environment variables (if needed)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Define the command to run the application
CMD ["opentelemetry-instrument", "flask", "run", "--host=0.0.0.0"]