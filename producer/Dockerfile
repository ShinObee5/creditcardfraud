FROM python:3.9.14-slim-buster


# Actually install the application
WORKDIR /usr/src/app
# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY requirements.txt .
COPY sampledat.csv .
RUN apt-get update
RUN pip install -r requirements.txt
COPY producer.py .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "/usr/src/app/producer.py"]