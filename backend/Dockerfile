FROM python:3.9.14-slim-buster

WORKDIR /usr/src/app
# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY requirements.txt .
RUN apt-get update 
RUN pip install -r requirements.txt
RUN apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY templates/home.html templates/home.html
COPY app.py .
COPY model.py .
# When you just 'docker run publisher' with no command afterwards,
# default to this:
EXPOSE 8000
CMD ["python", "/usr/src/app/app.py"]