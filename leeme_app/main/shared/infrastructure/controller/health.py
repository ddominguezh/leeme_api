from fastapi import APIRouter

from leeme_app.main.shared.infrastructure.controller.health_response import HealthResponse

health_router = APIRouter()

@health_router.get("/api/v1/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status=True)