FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

ENV SHELL=/bin/bash
ENV DEBIAN_FRONTEND=noninteractive
ENV PIPENV_VENV_IN_PROJECT=1
ENV VIRTUAL_ENV=/workspaces/graduation_project/.venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH

WORKDIR /workspace/graduation_project/

RUN echo 'alias pip="pipenv -v"' >> ~/.bashrc

RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg -y
RUN apt-get autoremove -y

RUN pip install pipenv