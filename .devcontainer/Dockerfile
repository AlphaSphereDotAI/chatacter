FROM mcr.microsoft.com/devcontainers/base:ubuntu

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg -y
RUN apt-get install python3-pip git -y
RUN apt-get autoremove -y

RUN pip install -v -U pip
RUN pip install -v setuptools==59.8.0
RUN pip install -v torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio --use-pep517 --extra-index-url https://download.pytorch.org/whl/cu121
RUN pip install -v basicsr==1.4.2 --use-pep517
RUN pip install -v -r requirements.txt