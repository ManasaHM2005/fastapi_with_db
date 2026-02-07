from fastapi import FastAPI
from routes.user_routtes import router as user_router
from db import get_db,DATABASE_URL
from sqlalchemy import create_engine
from model import Base
import os
app = FastAPI()

app.include_router(user_router)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000,reload=True)
