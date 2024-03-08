from fastapi import FastAPI
from fastapi.responses import FileResponse

from model import get_response

app = FastAPI(title="Hello world", description="This is a hello world example")


@app.get("/")
async def hello_world():
    return "hello world"


@app.post("/predict")
def predict(query: str):
    """predict function"""
    return get_response(query)


@app.get("/download")
def download_file():
    return FileResponse("./assets/demo.gif")
