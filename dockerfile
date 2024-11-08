# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . .

# Install the necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 6000
EXPOSE 6000

# Set the command to run the Flask app
CMD ["python", "app.py"]

