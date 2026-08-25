import httpx


RAG_API_URL = "http://localhost:8001"


async def search_rag(
    query: str,
    top_k: int = 5,
) -> dict:

    async with httpx.AsyncClient(
        timeout=30
    ) as client:

        response = await client.post(
            f"{RAG_API_URL}/documents/search",
            json={
                "query": query,
                "top_k": top_k,
            },
        )

        response.raise_for_status()

        return response.json()