# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Set the CUSTOM_KNOWLEDGE_DIRECTORY environment variable
ENV CUSTOM_KNOWLEDGE_DIRECTORY=/app/custom_knowledge

# Copy the entire project into the container
COPY . /app/

# Run your Python application
CMD ["python", "app.py"]
