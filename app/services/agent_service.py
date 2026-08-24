import uuid

from app.agents.graph import agent_graph


async def run_agent(
    message: str,
    conversation_id: str | None = None,
):

    conversation_id = (
        conversation_id
        or str(uuid.uuid4())
    )

    result = await agent_graph.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ],
            "tools_used": [],
        }
    )

    last_message = result["messages"][-1]

    return {
        "conversation_id": conversation_id,
        "answer": last_message.content,
        "tools_used": result.get(
            "tools_used",
            [],
        ),
    }