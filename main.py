from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
async def main():
    print(f'Logging from {__name__}')
    return {"message": "Hello World"}

Instrumentator().instrument(app).expose(app)