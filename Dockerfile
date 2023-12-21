# Base image with GUI support
FROM ubuntu:22.04

# Install essential dependencies
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    x11-apps \
    x11-utils \
    xauth \
    xvnc4server

# Set up a virtual environment for Python
RUN python3.12 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Python GUI dependencies (replace with your specific requirements)
RUN pip install tkinter

# Copy your Python GUI application files to the container
COPY ./app /app

# Set the working directory
WORKDIR /app

# Expose ports for VNC and any other application ports
EXPOSE 5901  # VNC port

# Start VNC Server and your Python GUI application
CMD ["vncserver", "-geometry", "1280x1024", ":0", "-depth", "24"]
CMD ["python", "new.py"]  # Replace with your application's main file
