from fastapi import FastAPI
from app.routers import company, user, payment
from app.database.connection import create_db

app = FastAPI()
create_db()

app.include_router(company.router)
app.include_router(user.router)
app.include_router(payment.router)