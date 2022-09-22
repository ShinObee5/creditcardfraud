FROM python:3.9.14-alpine3.16


# Actually install the application
WORKDIR /usr/src/app
# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY requirements.txt .
COPY sampledat.csv .
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN pip install -r requirements.txt
COPY producer.py .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "/usr/src/app/producer.py"]