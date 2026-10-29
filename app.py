from fastapi import FastAPI
from incident_agent import router

app = FastAPI()
app.include_router(router)
