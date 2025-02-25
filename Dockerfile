# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for git, curl, make, and age
RUN apt-get update && apt-get install -y \
    git \
    curl \
    make \
    gnupg \
    lsb-release \
    && apt-get clean

# Install uv
RUN pip3 install uv

# Install 'age' from its official GitHub release
RUN apt-get install age

# Generate key pairs for 'age'
RUN mkdir $HOME/.passage \
    && age-keygen -o $HOME/.passage/identities

# Clone the passage repo
RUN git clone https://github.com/FiloSottile/passage

# Set the working directory to the 'passage' directory
WORKDIR /app/passage

# Install 'passage' using Make
RUN make install

# Write some dummy passwords
RUN passage generate personal/demo/demo1@gmail.com
RUN passage generate personal/demo/demo2@gmail.com
RUN passage generate personal/demo/demo3@gmail.com
RUN passage generate work/workdemo1@gmail.com
RUN passage generate work/workdemo2@gmail.com
RUN passage generate work/workdemo3@gmail.com

# Clone the GitHub repository for the web UI
WORKDIR /app
RUN git clone https://github.com/ThangaAyyanar/passage-webui

# Set the working directory to the 'passage-webui' directory
WORKDIR /app/passage-webui

# Expose the port the app runs on
EXPOSE 8000

# run the fast api server
CMD ["uv", "run", "fastapi", "run", "main.py"]
