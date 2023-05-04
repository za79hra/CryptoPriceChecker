# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN pip install django-celery-beat


# Copy the rest of the application code
COPY . /code/

EXPOSE 8000
# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
