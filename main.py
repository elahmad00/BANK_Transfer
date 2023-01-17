from fastapi import FastAPI
import models 
from database import engine

app = FastAPI(title="Bank App",description="Providing multiple payment gateways")



models.Base.metadata.create_all(bind=engine)

#app.include_router(authentication.router)
#app.include_router(post.router)
#app.include_router(users.router)
#app.include_router(banking.router)

@app.get("/")
async def home():
    return {"home":"homepage on"}