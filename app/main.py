from fastapi import FastAPI

from app import config
from app.api.api_v1 import api

# Init fastAPI APP
app = FastAPI(
    title=config.PROJECT_NAME
)

# Include router
app.include_router(api.router)
