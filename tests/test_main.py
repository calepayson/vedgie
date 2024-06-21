from fastapi.testclient import TestClient

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

class TestHome:
    response = client.get("/")

    def test_read_home(self):
        assert self.response.status_code == 200
        assert self.response.headers["content-type"] == "text/html; charset=utf-8"
    
    def test_home_header(self):
        assert "<header>" in self.response.text
    
    def test_home_content(self):
        assert "<main>" in self.response.text
    
    def test_home_footer(self):
        assert "<footer>" in self.response.text

class TestBio:
    response = client.get("/bio")

    def test_read_bio(self):
        assert self.response.status_code == 200
        assert self.response.headers["content-type"] == "text/html; charset=utf-8"
    
    def test_bio_header(self):
        assert "<header>" in self.response.text
    
    def test_bio_content(self):
        assert "<main>" in self.response.text
    
    def test_bio_footer(self):
        assert "<footer>" in self.response.text

class TestMedia:
    response = client.get("/media")

    def test_read_media(self):
        assert self.response.status_code == 200
        assert self.response.headers["content-type"] == "text/html; charset=utf-8"
    
    def test_media_header(self):
        assert "<header>" in self.response.text
    
    def test_media_content(self):
        assert "<main>" in self.response.text
    
    def test_media_footer(self):
        assert "<footer>" in self.response.text

    def test_image_in_media(self):
        assert "<img" in self.response.text

class TestWriting:
    response = client.get("/writing")

    def test_read_writing(self):
        assert self.response.status_code == 200
        assert self.response.headers["content-type"] == "text/html; charset=utf-8"
    
    def test_writing_header(self):
        assert "<header>" in self.response.text
    
    def test_writing_content(self):
        assert "<main>" in self.response.text
    
    def test_writing_footer(self):
        assert "<footer>" in self.response.text
