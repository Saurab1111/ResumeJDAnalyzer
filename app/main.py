from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Resume JD Analyzer")

app.include_router(router)
