# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the application code, including static and template directories
COPY app /app

# Install dependencies
RUN pip install fastapi uvicorn jinja2

# Expose FastAPI's default port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
