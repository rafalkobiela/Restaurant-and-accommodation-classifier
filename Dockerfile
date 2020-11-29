# pull official base image
FROM ubuntu:18.04
RUN apt update

ARG PYTHON_VER="3.8"

RUN apt -y install python$PYTHON_VER-dev python$PYTHON_VER-distutils
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python$PYTHON_VER 2
RUN apt -y install wget mc nano vim libgomp1
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py


RUN mkdir -p /usr/src/app

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/usr/src"

RUN pip install --upgrade pip setuptools wheel

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0