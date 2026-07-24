from fastapi import APIRouter
from semiconops.core.config import get_settings

router = APIRouter(tags=["system"])

@router.get("/health")
def health() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }
