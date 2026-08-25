from langchain_core.tools import tool


@tool
def search_knowledge_base(
    query: str,
) -> dict:
    """
    Search the company's internal knowledge base.
    Use this when the user asks about company policies,
    documentation, procedures, or information that may
    exist inside internal documents.
    """

    # Temporary implementation.
    # We will connect this to Project 1's pgvector
    # retrieval pipeline in the next stage.

    return {
        "query": query,
        "results": [
            {
                "content": (
                    "Internal knowledge base search "
                    "will be connected to the RAG system."
                )
            }
        ],
    }