# Use a Debian-based Python image as the base image
FROM python:3.8-slim-buster

# Install espeak for pyttsx3 on Linux
RUN apt-get update && \
    apt-get install -y espeak && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the app directory into the container
COPY ./app /app

# Set the working directory
WORKDIR /app

# Install your app's Python dependencies
# Assuming you have a requirements.txt file in the app/ directory
RUN pip install -r requirements.txt

# Run your app
CMD ["python", "app.py"]
