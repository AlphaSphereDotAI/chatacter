FROM nginx:alpine
RUN apk update && \
    apk upgrade && \
    apk add bash curl git openssh-client openssl-dev build-base libffi-dev py3-pip python3
WORKDIR ${HOME}/app
RUN pip install Django
COPY . ${HOME}/app
CMD [ "python", "manage.py", "runserver"]