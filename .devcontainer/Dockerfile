FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

ENV SHELL=/bin/bash
ENV DEBIAN_FRONTEND=noninteractive
ENV PIPENV_VENV_IN_PROJECT=1

RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg -y
RUN apt-get autoremove -y

WORKDIR /workspaces/graduation_project/

RUN pip install -v -U pip uv pipenv
RUN pipenv install -v setuptools==59.8.0
RUN pipenv install -v torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio -i https://download.pytorch.org/whl/cu121
RUN pipenv install -v basicsr==1.4.2
RUN pipenv install -v -r requirements.txt
RUN pipenv shell