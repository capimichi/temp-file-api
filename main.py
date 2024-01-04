import mimetypes

from fastapi import FastAPI, HTTPException
from typing import Dict
from pydantic import BaseModel
import base64
import json
import hashlib
import time
import os
import imghdr
import glob
import uvicorn
from starlette.responses import FileResponse

app = FastAPI()

MEDIA_DIRECTORY = 'media'

class Image(BaseModel):
    image: str

@app.post("/upload")
async def upload_file(body: Image):
    image_data = base64.b64decode(body.image)
    file_id = hashlib.md5(str(time.time()).encode()).hexdigest()
    os.makedirs(MEDIA_DIRECTORY, exist_ok=True)
    image_type = imghdr.what(None, h=image_data)
    file_path = f"{MEDIA_DIRECTORY}/{file_id}.{image_type}"
    with open(file_path, "wb") as f:
        f.write(image_data)
    return {
        "id": file_id
    }

@app.get("/medias/{id}")
async def get_media(id: str):
    files = glob.glob(f"{MEDIA_DIRECTORY}/{id}.*")
    if not files:
        raise HTTPException(status_code=404, detail="Media not found")
    return FileResponse(files[0], media_type=mimetypes.guess_type(files[0])[0])

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=os.getenv('HOST', '127.0.0.1'), 
        port=int(os.getenv('PORT', 8500))
    )