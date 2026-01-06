import psycopg2
from psycopg2.extras import execute_batch
from config.config import DB_CONFIG


def load(df):
    """
    Load transformed DataFrame into PostgreSQL.
    """

    if df.empty:
        return

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO sales
        (order_id, order_date, product, quantity, price, total_amount, customer_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    records = [
        (
            row.order_id,
            row.order_date,
            row.product,
            row.quantity,
            row.price,
            row.total_amount,
            row.customer_id,
        )
        for row in df.itertuples(index=False)
    ]

    execute_batch(cur, insert_query, records, page_size=100)

    conn.commit()
    cur.close()
    conn.close()
