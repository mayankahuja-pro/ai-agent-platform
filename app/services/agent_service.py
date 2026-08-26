import uuid

from langchain_core.messages import (
    messages_from_dict,
    messages_to_dict,
    HumanMessage,
    AIMessage,
)

from app.agents.graph import agent_graph
from app.services.redis_service import (
    get_conversation,
    save_conversation,
)

import logging

logger = logging.getLogger(__name__)

async def run_agent(
    message: str,
    conversation_id: str | None = None,
):

    conversation_id = (
        conversation_id
        or str(uuid.uuid4())
    )

    logger.info(
        "Starting agent conversation=%s",
        conversation_id,
    )

    previous_messages_raw = await get_conversation(
        conversation_id
    )

    previous_messages = []
    if previous_messages_raw:
        try:
            previous_messages = messages_from_dict(
                previous_messages_raw
            )
        except Exception:
            for msg in previous_messages_raw:
                role = msg.get("role")
                content = msg.get("content", "")
                if role in ("user", "human"):
                    previous_messages.append(
                        HumanMessage(content=content)
                    )
                elif role in ("ai", "assistant"):
                    previous_messages.append(
                        AIMessage(content=content)
                    )

    messages = [
        *previous_messages,
        HumanMessage(content=message),
    ]

    result = await agent_graph.ainvoke(
        {
            "messages": messages,
            "tools_used": [],
            "iterations": 0,
        }
    )

    final_messages = result["messages"]

    last_message = final_messages[-1]

    await save_conversation(
        conversation_id,
        messages_to_dict(final_messages),
    )

    tools_used = []

    for msg in final_messages:

        if hasattr(msg, "name") and msg.name:
            tools_used.append(msg.name)

    tools_used = list(dict.fromkeys(tools_used))
    
    logger.info(
        "Agent completed conversation=%s tools=%s",
        conversation_id,
        tools_used,
    )        
    return {
        "conversation_id": conversation_id,
        "answer": last_message.content,
        "tools_used": tools_used,
    }