import json

from redis.asyncio import Redis

from app.config import settings


redis = Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
)


async def save_conversation(
    conversation_id: str,
    messages: list,
):
    key = f"conversation:{conversation_id}"

    await redis.set(
        key,
        json.dumps(messages),
        ex=60 * 60 * 24,
    )


async def get_conversation(
    conversation_id: str,
):
    key = f"conversation:{conversation_id}"

    data = await redis.get(key)

    if not data:
        return []

    return json.loads(data)


async def delete_conversation(
    conversation_id: str,
):
    key = f"conversation:{conversation_id}"

    await redis.delete(key)