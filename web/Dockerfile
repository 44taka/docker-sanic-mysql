FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip uninstall -r requirements.txt
RUN pip install -r requirements.txt
ADD . /code/
