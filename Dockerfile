# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the chatbot
EXPOSE 8080

# Run chatbot when the container launches
CMD ["python", "chatbot_with_emotion_detection.py"]
