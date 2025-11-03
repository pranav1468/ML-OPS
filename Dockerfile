FROM python:3.10-slim

LABEL maintainer="Pranav Baghare <pranavbaghare46@gmail.com>"

WORKDIR /main

RUN pip install numpy

COPY . /main

CMD ["python", "main.py"]
