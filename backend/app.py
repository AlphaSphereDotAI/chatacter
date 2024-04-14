import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from model import get_response

app = FastAPI()


@app.get("/")
async def hello_world():
    """hello world function"""
    return "hello world"


@app.post("/predict")
def predict(query: str):
    """predict function"""
    return get_response(query)


@app.get("/download")
def download_file():
    """download the file"""
    return FileResponse("./assets/demo.wav", media_type="audio/wav")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
