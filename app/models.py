from sqlalchemy import Column, Integer, String
from .database import Base

class GlossaryItem(Base):
    __tablename__ = "glossary"

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
