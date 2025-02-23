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

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install 'age' from its official GitHub release
RUN apt install age

# Generate key pairs for 'age'
RUN mkdir $HOME/.passage \
    && age-keygen -o $HOME/.passage/identities

# Clone the passage repo
RUN git clone https://github.com/FiloSottile/passage

# Set the working directory to the 'passage' directory
WORKDIR /app/passage

# Install 'passage' using Make
RUN make install

# Clone the GitHub repository for the web UI
WORKDIR /app
RUN git clone https://github.com/ThangaAyyanar/passage-webui

# Set the working directory to the 'passage-webui' directory
WORKDIR /app/passage-webui

# Install Python dependencies for the web UI using Poetry
RUN poetry install

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
