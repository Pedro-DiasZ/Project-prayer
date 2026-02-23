from fastapi import FastAPI
from schemas import PraySchema

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/Prayer")
def create_pray(pray: PraySchema):
    return pray