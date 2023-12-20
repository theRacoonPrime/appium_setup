# Use an official Python runtime as a parent image
 FROM python:3.10-slim

 # Set the working directory in the container
 WORKDIR /app

 # Install necessary dependencies
 RUN apt-get update -y && apt-get install -y \
     build-essential \
     wget \
     unzip

 # Install Appium
 RUN npm install -g appium

 # Install ChromeDriver for Selenium
 RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
     wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
     unzip chromedriver_linux64.zip && \
     mv chromedriver /usr/local/bin/

 # Copy the current directory contents into the container at /app
 COPY . /app

 # Install Poetry
 RUN pip install poetry

 # Install project dependencies
 RUN poetry install

 # Make port 4723 available to the world outside this container
 EXPOSE 4723

 # Define environment variable for Appium
 ENV ANDROID_HOME=/path/to/your/android/sdk

 # Run appium when the container launches
 CMD ["appium"]