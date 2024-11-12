from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return 'Hello, the server is working'

