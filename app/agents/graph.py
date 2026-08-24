from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.agents.state import AgentState


def dummy_agent(state: AgentState):

    return {
        "messages": [
            {
                "role": "assistant",
                "content": "Agent is working.",
            }
        ]
    }


builder = StateGraph(AgentState)

builder.add_node(
    "agent",
    dummy_agent,
)

builder.add_edge(
    START,
    "agent",
)

builder.add_edge(
    "agent",
    END,
)

agent_graph = builder.compile()