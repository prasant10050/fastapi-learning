import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from storeapi.database import database
from storeapi.logging_config import configure_logging
from storeapi.routers.post import router as post_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger.info("Database conneting...")
    await database.connect()
    logger.info("Database connected.")
    yield
    await database.disconnect()
    logger.info("Database disconnected.")


app = FastAPI(lifespan=lifespan)

app.include_router(post_router)
# app.include_router(post_router,prefix="/posts")
