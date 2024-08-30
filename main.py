from fastapi import FastAPI
from routers import router, requests_client


app = FastAPI()
app.requests_client = requests_client
app.include_router(router)
