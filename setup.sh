#!/bin/bash

# Update package list and install required dependencies
echo "Updating package list and installing dependencies..."
sudo apt-get update && sudo apt-get install -y \
    git \
    curl \
    make \
    gnupg \
    lsb-release \
    age

# Install `uv` (Uvicorn or uv dependency tool, depending on your need)
echo "Installing uv..."
pip3 install uv

# Generate key pairs for 'age'
echo "Generating key pairs for 'age'..."
mkdir -p $HOME/.passage
age-keygen -o $HOME/.passage/identities

# Clone the 'passage' repository
echo "Cloning the Passage repository..."
git clone https://github.com/FiloSottile/passage

# Change to the 'passage' directory
cd passage

# Install Passage using Make
echo "Installing Passage..."
make install

# Generate some dummy passwords for different folders
echo "Generating passwords..."
passage generate personal/demo/demo1@gmail.com
passage generate personal/demo/demo2@gmail.com
passage generate personal/demo/demo3@gmail.com
passage generate work/workdemo1@gmail.com
passage generate work/workdemo2@gmail.com
passage generate work/workdemo3@gmail.com

# Go back to the main directory
cd ..

# Clone the 'passage-webui' repository for the web interface
echo "Cloning the Passage WebUI repository..."
git clone https://github.com/ThangaAyyanar/passage-webui

# Change to the 'passage-webui' directory
cd passage-webui

# Expose port 8000 (this will be done inside Docker or server environment)
echo "Exposing port 8000 for the app..."

# Assuming FastAPI is running with uvicorn, ensure uvicorn is installed
echo "Installing uvicorn..."
pip install uvicorn

# Run the FastAPI application using uvicorn
echo "Running FastAPI app..."
uvicorn main:app --host 0.0.0.0 --port 8000

