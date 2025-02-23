# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi uvicorn numpy pydantic scikit-learn

# Expose port 8080 (Required for Google Cloud Run)
EXPOSE 8080

# Run FastAPI using Uvicorn and read PORT dynamically
CMD ["python", "app.py"]
