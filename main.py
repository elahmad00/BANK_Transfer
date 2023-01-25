from fastapi import FastAPI
import models 
from database import engine
from router import banking



app = FastAPI(title="Bank App",description="Providing multiple payment gateways")



models.Base.metadata.create_all(bind=engine)


app.include_router(banking.router)

@app.get("/")
async def home():
    return {"home":"homepage on"}