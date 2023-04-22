# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8001 for the Flask app to listen on
EXPOSE 8001

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Run the Flask application when the container starts
CMD ["python", "main.py"]