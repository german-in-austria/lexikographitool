# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /backend

# Set the working directory to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
ADD . /backend/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt