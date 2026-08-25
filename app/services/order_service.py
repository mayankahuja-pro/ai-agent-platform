from sqlalchemy import select

from app.database import SessionLocal
from app.models.order import Order


def find_order(
    order_id: str,
) -> dict:

    db = SessionLocal()

    try:

        statement = select(Order).where(
            Order.order_id == order_id
        )

        order = db.scalar(statement)

        if not order:

            return {
                "found": False,
                "order_id": order_id,
            }

        return {
            "found": True,
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "status": order.status,
            "amount": order.amount,
            "currency": order.currency,
        }

    finally:
        db.close()