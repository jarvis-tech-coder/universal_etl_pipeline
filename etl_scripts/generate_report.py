import pandas as pd
import psycopg2
from config.config import DB_CONFIG, REPORT_PATH


def generate_report():
    """
    Generate aggregated sales report from PostgreSQL
    and save it as an Excel file.
    """

    conn = psycopg2.connect(**DB_CONFIG)

    query = """
        SELECT
            product,
            SUM(quantity) AS total_units,
            SUM(total_amount) AS total_revenue
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC;
    """

    df = pd.read_sql(query, conn)
    df.to_excel(REPORT_PATH, index=False)

    conn.close()
