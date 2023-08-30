from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.configs import settings
from  .api.api_v1.router import router
from .core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS
)

app.include_router(router)
