# Use an Ubuntu-based image
FROM ubuntu:20.04

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Essential tools and libraries
RUN apt-get clean
RUN apt-get update 
RUN apt-get install -y --fix-missing \
    festival \
    wget \
    unzip \
    python3 \
    python3-pip

# Fetch and install the CMU Arctic voices for Festival
WORKDIR /opt
RUN wget http://festvox.org/cmu_arctic/cmu_arctic/packed/cmu_us_bdl_arctic-0.95-release.tar.bz2
RUN tar -xjf cmu_us_bdl_arctic-0.95-release.tar.bz2
RUN mv cmu_us_bdl_arctic /usr/share/festival/voices/english/

# Copy the app directory into the container
COPY ./app /app

# Set the working directory
WORKDIR /app

# Create audio_files directory within the container
RUN mkdir audio_files

# Install your app's Python dependencies
# Assuming you have a requirements.txt file in the app/ directory
RUN pip3 install -r requirements.txt

# Run your app
CMD ["python3", "app.py"]
