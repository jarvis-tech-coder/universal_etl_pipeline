import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize schema and apply business transformations.
    Input: Raw DataFrame from extract layer
    Output: Clean, analytics-ready DataFrame
    """

    # ---- Schema Normalization (handle JSON/API naming) ----
    df = df.rename(columns={
        "orderId": "order_id",
        "orderDate": "order_date",
        "qty": "quantity",
        "unitPrice": "price",
        "customerId": "customer_id"
    })

    # ---- Type Casting ----
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # ---- Business Logic ----
    df["total_amount"] = df["quantity"] * df["price"]

    # ---- Data Quality (light, production-safe) ----
    df = df.dropna(subset=["order_id", "order_date", "product", "quantity", "price"])
    df = df.drop_duplicates()

    return df
