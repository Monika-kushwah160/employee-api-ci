from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello Fastapi"}


@app.get("/home")
def home():
  return {"message": "Welcome to my page"}