# read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile
FROM python:3.10
COPY . ./code
WORKDIR /code
RUN pip install uv -U
RUN uv pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
