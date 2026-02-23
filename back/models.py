from sqlalchemy import Column, Integer, String
from database import Base

class Prayer(Base):
    __tablename__ = "prayers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    prayer = Column(String, nullable=False)