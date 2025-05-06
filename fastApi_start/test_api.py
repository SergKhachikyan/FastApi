import pytest
from httpx import AsyncClient, ASGITransport
from fastApi_start.books import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url="http://test") as ac:
        response = await ac.get("/books")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

@pytest.mark.asyncio
async def test_post_books():
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url="http://test") as ac:
        response = await ac.post("/books", json={
            "title": "Name",
            "author": "Matthew",
        })
        assert response.status_code == 200
        data = response.json()
        assert data == {"success": True, "message": "Book was added"}
