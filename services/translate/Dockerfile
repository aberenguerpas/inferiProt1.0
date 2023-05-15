FROM python:3.10
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install torch
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port 8001