from fastapi.testclient import TestClient

from app.config import Settings
from app.main import create_app

test_app = create_app(
    Settings(allowed_origins="http://localhost:5173")
)

client = TestClient(test_app)

def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status" : "ok"}

def test_cors_allows_frontend_origin() -> None:
    response = client.options(
        "/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method" : "GET",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"