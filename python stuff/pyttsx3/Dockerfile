# Use an Ubuntu-based image
FROM ubuntu:20.04

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies, espeak, ffmpeg, and mbrola voices
RUN apt-get update && \
    apt-get install -y espeak ffmpeg wget python3-pip mbrola mbrola-us1 mbrola-us2 mbrola-us3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the app directory into the container
COPY ./app /app

# Set the working directory
WORKDIR /app

# Install your app's Python dependencies
# Assuming you have a requirements.txt file in the app/ directory
RUN pip3 install -r requirements.txt

# Run your app
CMD ["python3", "app.py"]
