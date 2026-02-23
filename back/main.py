from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import PraySchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/Prayer")
def create_pray(pray: PraySchema):
    return pray