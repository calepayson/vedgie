from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse(request=request, name="home_content.html")

@app.get("/bio", response_class=HTMLResponse)
def read_bio(request: Request):
    return templates.TemplateResponse(request=request, name="bio_content.html")

@app.get("/media", response_class=HTMLResponse)
def read_media(request: Request):
    return templates.TemplateResponse(request=request, name="media_content.html")

@app.get("/writing", response_class=HTMLResponse)
def read_writing(request: Request):
    return templates.TemplateResponse(request=request, name="writing_content.html")
