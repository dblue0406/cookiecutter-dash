FROM manifoldai/orbyter-ml-dev:4.1
LABEL maintainer="{{cookiecutter.author_name}} <{{cookiecutter.author_email}}>"

RUN apt-get update

COPY /docker/requirements.txt /build/requirements.txt
WORKDIR /build/
RUN pip install -r /build/requirements.txt

COPY . /app
WORKDIR /app
