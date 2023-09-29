# Use the official Python image
FROM python:3.9-slim-buster

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY app.py /app/app.py

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

