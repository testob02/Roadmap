import utils
from fastapi import FastAPI


app = FastAPI()
 

utils.load_artifacts()


@app.post('/classify_image')
async def classify_image(request: utils.InputSchema):
    return utils.classify(request)