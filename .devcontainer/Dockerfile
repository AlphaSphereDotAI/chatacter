FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg -y
RUN apt-get install curl -y
RUN apt-get autoremove -y

# Node
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash 
RUN apt-get update
RUN apt-get install nodejs -y
RUN npx --yes dotenv-vault@latest

# Git
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install git-lfs -y

# CUDA
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
RUN apt-get update
RUN apt-get install nvidia-container-toolkit -y
RUN apt-get install nvidia-docker2 -y
RUN nvidia-ctk runtime configure --runtime=docker

# Environment Variables
ENV VIRTUAL_ENV=/workspaces/graduation_project/.venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH
ENV UV_EXTRA_INDEX_URL=https://download.pytorch.org/whl/cu121
ENV CWD=/workspaces/graduation_project/streamlit
ENV NVIDIA_VISIBLE_DEVICES=all

# Alias
RUN echo 'alias pip="uv -v pip"' >> ~/.bashrc
RUN echo 'alias py="python"' >> ~/.bashrc
RUN echo 'alias env="npx -yes dotenv-vault"' >> ~/.bashrc
RUN echo 'source /workspaces/graduation_project/.venv/bin/activate' >> ~/.bashrc