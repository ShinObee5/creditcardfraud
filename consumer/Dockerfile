FROM python:3.9.14-slim-buster

WORKDIR /usr/src/app
# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY requirements.txt .
RUN apt-get update 
RUN pip install -r requirements.txt
COPY consumer.py .
COPY model.pkl .
COPY templates/home.html templates/home.html
COPY app.py .
COPY processed.csv .
COPY start.sh .
# When you just 'docker run publisher' with no command afterwards,
# default to this:
EXPOSE 8000
CMD ["bash", "/usr/src/app/start.sh"]