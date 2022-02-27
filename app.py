
import re
from fastapi import FastAPI ,Request,UploadFile,File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import HTMLResponse,FileResponse
import io
import os
import time
import pathlib
from PIL import Image



app  = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
    max_age=10
    )


app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

@app.get("/",response_class=HTMLResponse)
def read(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})



@app.post("/count_rice")
async def count_rice(image:UploadFile=File(...)):

    str_bytes =io.BytesIO(await image.read())

    try:
        img = Image.open(str_bytes)
    except:
        raise HTTPException(status_code=400,detail='invalid image')

    return "s"
    
if __name__ == "__main__":
    uvicorn.run(app,port=8080)