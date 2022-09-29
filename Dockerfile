# syntax=docker/dockerfile:1

# base image
FROM python:3.8

# ~python -B
ENV PYTHONDONTWRITEBYTECODE=1
# log in console ~ python -u
ENV PYTHONUNBUFFERED=1

ENV PORT 8000

# set work directory
WORKDIR /code

# copy just the requirements.txt first to leverage Docker cache
# install all dependencies for Python app
# what-where
COPY requirements.txt requirements.txt

# update pip & install dependencies in requirements.txt
RUN python -m pip install --upgrade pip \ 
&& pip install -r requirements.txt

# copy all content to work directory /app
COPY . .

# run the application
CMD gunicorn oc_lettings_site.wsgi -b 0.0.0.0:$PORT