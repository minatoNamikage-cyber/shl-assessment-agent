from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router

from app.core.config import settings
from app.core.logging import logger

from app.services.catalog_service import catalog_service

from app.api.llm import router as llm_router

from app.api.chat import router as chat_router



# FIRST create app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# THEN include routers
app.include_router(chat_router)
app.include_router(health_router)
app.include_router(llm_router)
app.include_router(chat_router)


@app.on_event("startup")
async def startup():
    logger.info("Application Started")

@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }
@app.on_event("startup")
async def startup():

    logger.info("Starting SHL Assessment Agent...")

    catalog_service.load_catalog()

    logger.success("Application Ready.")