from langchain_core.tools import tool


ORDERS = {
    "1001": {
        "order_id": "1001",
        "customer": "Rahul",
        "status": "shipped",
        "amount": 2499,
        "currency": "INR",
    },
    "1002": {
        "order_id": "1002",
        "customer": "Priya",
        "status": "delivered",
        "amount": 1599,
        "currency": "INR",
    },
    "1003": {
        "order_id": "1003",
        "customer": "Amit",
        "status": "processing",
        "amount": 3999,
        "currency": "INR",
    },
}


@tool
def get_order(order_id: str) -> dict:
    """
    Get order information using the order ID.
    """

    order = ORDERS.get(order_id)

    if not order:
        return {
            "error": f"Order {order_id} was not found."
        }

    return order