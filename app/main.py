import config
from api.api_v1 import api
from fastapi import FastAPI

# Init fastAPI APP
app = FastAPI(
    title=config.PROJECT_NAME
)

# Include router
app.include_router(api.router)
