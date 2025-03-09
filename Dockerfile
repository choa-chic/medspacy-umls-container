# Use the official Python Alpine image
FROM python:3.12-alpine

# Install necessary packages
RUN apk update && \
    apk add --no-cache gcc g++ musl-dev \
    python3-dev wget leveldb

# Install pip packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests spacy medspacy medspacy-quickumls

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Run a command to keep the container running
CMD ["tail", "-f", "/dev/null"]