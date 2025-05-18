from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))