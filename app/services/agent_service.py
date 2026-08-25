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

    messages = result["messages"]

    tools_used = []

    for msg in messages:

        if hasattr(msg, "name") and msg.name:
            tools_used.append(msg.name)

    last_message = messages[-1]

    return {
        "conversation_id": conversation_id,
        "answer": last_message.content,
        "tools_used": list(
            dict.fromkeys(tools_used)
        ),
    }