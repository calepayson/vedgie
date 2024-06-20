from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_home():
    return {"message": "Hello, World"}
