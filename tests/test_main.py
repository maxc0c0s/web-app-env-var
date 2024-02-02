from fastapi.testclient import TestClient
from web_app_env_var.main import app
import os

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"MESSAGE": os.getenv("MESSAGE")}
