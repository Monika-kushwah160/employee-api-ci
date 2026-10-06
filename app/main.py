from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello Fastapi"}


@app.get("/home")
def home():
    return {"message": "Welcome to my page"}


@app.get("/employee")
def employee():
    return {"message": "Hello !"}


@app.get("/demo")
def demo():
    return {"message": "Welcome to my new blog"}
