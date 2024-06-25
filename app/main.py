from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown2
import os
from pydantic import BaseModel

from .utils.lib import file_name_to_title


class ArticleMetaData(BaseModel):
    file_name: str
    title: str


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
    images = os.listdir("static/images/")
    return templates.TemplateResponse(
            request=request, 
            name="media_content.html", 
            context={"images": images}
            )

@app.get("/writing", response_class=HTMLResponse)
def read_writing(request: Request):
    articles = []
    for f in os.listdir("static/articles"):
        articles.append(ArticleMetaData(
            file_name=f,
            title=file_name_to_title(f)
        ))

    return templates.TemplateResponse(
            request=request, 
            name="writing_content.html", 
            context={"articles":articles}
            )

@app.get("/writing/{file_name}", response_class=HTMLResponse)
def read_article(request: Request, file_name: str):
    file_path = f"static/articles/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File not found: {file_name}")
    with open(file_path, "r") as file:
        markdown_text = file.read()
    html_content = markdown2.markdown(markdown_text)
    return templates.TemplateResponse("article_content.html", {"request": request, "html_content": html_content})
