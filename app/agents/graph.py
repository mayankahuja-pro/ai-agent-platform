from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.agents.llm import llm
from app.agents.state import AgentState
from app.tools.order_tool import get_order


tools = [
    get_order,
]

llm_with_tools = llm.bind_tools(tools)


def agent_node(state: AgentState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)

builder.add_node(
    "agent",
    agent_node,
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