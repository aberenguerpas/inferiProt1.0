FROM python:3.10
RUN mkdir code
ADD requirements.txt /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install torch
RUN pip install -r requirements.txt

ADD . /code


CMD uvicorn main:app --host 0.0.0.0 --port 5000