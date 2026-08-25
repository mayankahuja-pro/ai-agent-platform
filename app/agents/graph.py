from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from langgraph.prebuilt import ToolNode

from app.agents.llm import llm
from app.agents.state import AgentState
from app.tools.calculator_tool import calculate
from app.tools.order_tool import get_order
from app.tools.search_tool import search_knowledge_base
from app.agents.prompts import SYSTEM_PROMPT
from langchain_core.messages import SystemMessage
tools = [
get_order,
calculate,
search_knowledge_base,
]

llm_with_tools = llm.bind_tools(tools)


def agent_node(state: AgentState):

    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT
        ),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [response]
    }


def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


tool_node = ToolNode(tools)


builder = StateGraph(AgentState)


builder.add_node(
    "agent",
    agent_node,
)

builder.add_node(
    "tools",
    tool_node,
)


builder.add_edge(
    START,
    "agent",
)


builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        END: END,
    },
)


builder.add_edge(
    "tools",
    "agent",
)


agent_graph = builder.compile()