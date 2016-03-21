#FROM python:2
FROM continuumio/miniconda:latest

RUN mkdir /app
VOLUME /app
WORKDIR /app

RUN conda install --yes Matplotlib

CMD ["python2"]
