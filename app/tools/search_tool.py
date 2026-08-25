from langchain_core.tools import tool

from app.services.rag_client import search_rag


@tool
async def search_knowledge_base(
    query: str,
) -> dict:
    """
    Search the internal company knowledge base.

    Use this tool for:
    - company policies
    - documentation
    - employee handbook information
    - internal procedures
    - information stored in company documents

    Do not use this tool for order information
    or mathematical calculations.
    """

    try:

        result = await search_rag(
            query=query,
            top_k=5,
        )

        return result

    except Exception:

        return {
            "error": "Knowledge base is currently unavailable."
        }