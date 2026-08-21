import os


def cors_origins() -> list[str]:
    """Return CORS origins configured for the current environment."""
    configured = os.getenv("ARCHMASTER_CORS_ORIGINS", "http://localhost:5173")
    return [origin.strip() for origin in configured.split(",") if origin.strip()]
