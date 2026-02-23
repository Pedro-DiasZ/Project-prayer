from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from schemas import PraySchema
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/prayer")
def create_pray(pray: PraySchema, db: Session = Depends(get_db)):
    db_pray = models.Prayer(name=pray.name, prayer=pray.prayer)
    db.add(db_pray)
    db.commit()
    db.refresh(db_pray)
    return db_pray
