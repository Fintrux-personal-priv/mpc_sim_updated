# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the simulation code into the container at /app
COPY mpc.py .

# Install required Python packages
RUN pip install flask

# Expose the necessary ports:
# - 5001: Return channel for Bank 1
# - 6001-6019: Secret sharing ports for banks 1 to 19
# - 7001-7019: Round-robin addition ports for banks 1 to 19
# - 8001-8019: API ports for banks 1 to 19
EXPOSE 5001 6001-6019 7001-7019 8001-8019

# Define the command to run the simulation
CMD ["python", "mpc.py"]
