from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(
    title='Messenger', openapi_url=f"/127.0.0.1/api/v1/openapi.json"
)


app.include_router(api_router, prefix="/api/v1")
