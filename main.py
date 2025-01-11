from sys import prefix

from fastapi import FastAPI, Query, Depends, Response
from routers import ItemRouter

app = FastAPI()

app.include_router(
    router=ItemRouter.router,
    tags=["items"],
    prefix="/items",
)


@app.get("/actuator/health", status_code=200)
def actuator_endpoint():
    return {"status": "UP"}
