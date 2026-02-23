from pydantic import BaseModel

class PraySchema(BaseModel):
    name: str
    prayer: str