FROM ubuntu

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update
RUN apt-get install python3-pip git -y
RUN python3 -m pip install --upgrade pip

COPY . /workspace
WORKDIR /workspace
RUN ls
RUN pip3 install -r requirements.txt