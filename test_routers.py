import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from main import app

BASE_URL = "http://web:8989"

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_get_forecast():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        json = {"user_id": "test_user"}
        response = await client.post("/forecast", json=json)
        assert response.status_code == 200
        assert response.json() == {"user_id": "test_user"}

@pytest.mark.asyncio
async def test_check_process():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.get("/check_process?user_id=test_user")
        assert response.status_code == 200
        assert response.json() == {"error": "User does not exist"}

@pytest.mark.asyncio
async def test_check_process():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.post("/check_process", json={"user_id": "test_user"})
        assert response.status_code == 200
        assert response.json() == {"error": "User does not exist"}