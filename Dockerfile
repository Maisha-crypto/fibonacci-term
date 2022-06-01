# syntax=docker/dockerfile:1

FROM python:3.10.4

ADD fibonacci_program.py .

RUN pip install numpy

CMD [ "python", "./fibonacci_program.py"]