from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database import db

app = FastAPI()

origins = ["http://localhost:3000"] # Assuming React runs on port 3000

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/kudos/", status_code=200)
def read_items():
    json_db = []
    for item in db:
        json_db.append(jsonable_encoder(item))

    return JSONResponse(json_db)