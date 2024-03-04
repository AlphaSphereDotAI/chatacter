FROM ubuntu

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

COPY . /workspace
WORKDIR /workspace
RUN ls
RUN pip3 install -r requirements.txt