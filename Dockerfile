# -------- COMMANDS TO USE THIS IMAGE --------

# Command to build the image file:
# docker build -t idansm/segmentation-server:1.0 . --platform linux/amd64
# remove '--platform linux/amd64' to build a docker image that is compatible with the host OS (On MacOS, on linux and windows keep the tag)

# Command to create a docker container from the image file created (running on port 8989 both internally in the container and on the outside):
# docker run --name segmentation-server -p 8989:8989 segmentation-server:1.0

# Command to run the docker container pulled from docker-hub:
# docker run --name segmentation-server -p 8989:8989 idansm/segmentation-server:1.0

# --------------------------------------------

# Use the official Python 3.8 base image
FROM python:3.8-slim-buster

## create a new directory for the server's docker files
#RUN mkdir /docker

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=server.py

# Expose the port on which the Flask server will run
EXPOSE 8989

# Start the Flask server
CMD ["bash", "run_server.sh"]
