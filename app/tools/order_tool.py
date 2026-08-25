from langchain_core.tools import tool

from app.services.order_service import find_order


@tool
def get_order(order_id: str) -> dict:
    """
    Retrieve order information using an order ID.
    Use this tool when the user asks about an order,
    including its status, customer, amount, or details.
    """

    return find_order(order_id)