# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
# Set work directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /code/

RUN pip install --no-cache-dir --index-url=https://pypi.org/simple/ -r requirements.txt

# Copy the rest of the application code
COPY ./ /code/

EXPOSE 8000
# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
