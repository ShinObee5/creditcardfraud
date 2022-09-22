FROM python:3.9.14-alpine3.16

WORKDIR /usr/src/app
# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY requirements.txt .
RUN apk update
RUN pip install -r requirements.txt
COPY consumer.py .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "/usr/src/app/consumer.py"]