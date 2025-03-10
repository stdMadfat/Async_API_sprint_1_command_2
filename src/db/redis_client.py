from redis.asyncio import Redis

from src.core.config import Settings
from src.utils.cache_service import CacheService

settings = Settings()

redis: Redis | None = None


async def get_redis() -> CacheService:
    global redis
    if not redis:
        redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    return CacheService(redis)
