FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

ENV SHELL=/bin/bash
ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/workspaces/graduation_project/.venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH
ENV UV_EXTRA_INDEX_URL=https://download.pytorch.org/whl/cu121
ENV CWD=/workspaces/graduation_project/streamlit

RUN echo 'alias pip="uv -v pip"' >> ~/.bashrc
RUN echo 'alias py="python"' >> ~/.bashrc

RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg -y
RUN apt-get autoremove -y