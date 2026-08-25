from app.database import SessionLocal
from app.models.order import Order


def seed_orders():

    db = SessionLocal()

    try:

        existing = db.query(Order).count()

        if existing > 0:
            print("Orders already exist.")
            return

        orders = [
            Order(
                order_id="1001",
                customer_name="Rahul",
                status="shipped",
                amount=2499,
                currency="INR",
            ),
            Order(
                order_id="1002",
                customer_name="Priya",
                status="delivered",
                amount=1599,
                currency="INR",
            ),
            Order(
                order_id="1003",
                customer_name="Amit",
                status="processing",
                amount=3999,
                currency="INR",
            ),
        ]

        db.add_all(orders)

        db.commit()

        print("Orders inserted.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_orders()