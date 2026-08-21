from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    """Report that the API is available."""
    return {"status": "ok"}
