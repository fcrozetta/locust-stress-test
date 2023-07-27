import time, random
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from .schemas.schemas import SuccessResponse, InputModel

rnd = random.Random()
app = FastAPI(
    title="API for stress tests",
    description="A simple API to show how we stress test using locust",
)


@app.get("/simple-get", tags=["Simple Examples"], response_model=SuccessResponse)
async def simple_get():
    response = SuccessResponse()
    return response


@app.get("/long-wait", tags=["Simple Examples"], response_model=SuccessResponse)
async def long_wait():
    time.sleep(rnd.randrange(3, 10))
    response = SuccessResponse()
    return response


@app.get("/random-failure", tags=["Simple Examples"], response_model=SuccessResponse)
async def random_failure():
    if rnd.random() >= 0.3:
        # time.sleep(1)
        return SuccessResponse()
    else:
        raise HTTPException(500)


@app.post("/input-process", tags=["Payload Examples"])
async def process(data: InputModel):
    response = SuccessResponse()
    return response


@app.get("/error", tags=["Error Examples"])
async def error():
    raise HTTPException(500, "Internal error")
