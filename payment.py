from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database.connection import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    status = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))