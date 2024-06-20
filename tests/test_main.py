from fastapi.testclient import TestClient

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

def test_home_header():
    response = client.get("/")
    assert "<header>" in response.text

def test_home_content():
    response = client.get("/")
    assert "<main>" in response.text

def test_home_footer():
    response = client.get("/")
    assert "<footer>" in response.text
