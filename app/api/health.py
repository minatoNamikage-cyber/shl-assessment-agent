from fastapi import APIRouter
from app.services.catalog_service import catalog_service

router = APIRouter()


@router.get("/health")
async def health():

    return {
        "status": "healthy",
        "catalog_loaded": catalog_service.is_loaded,
        "total_assessments": catalog_service.total_assessments
    }