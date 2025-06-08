# Use Python 3.11 image
FROM python:3.11



# Set non-interactive mode to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Ensure system is updated & dependencies are installed correctly
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft signing key & repository
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/keyrings/microsoft.asc \
    && echo "deb [signed-by=/etc/apt/keyrings/microsoft.asc] https://packages.microsoft.com/debian/11/prod bullseye main" | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update

# Install unixODBC separately to avoid conflicts
RUN apt-get install -y unixodbc unixodbc-dev

# Install Microsoft ODBC Driver 17
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17


# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for better caching)
COPY smartland/requirements.txt /app/


# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the full project
COPY . /app

# Change working directory to the Django project (where wsgi.py is located)
WORKDIR /app/smartland

# Run Django management commands
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

# Expose port 8000
EXPOSE 8000

# Start the Django application with daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "--application-close-timeout", "120", "smartland.asgi:application"]
