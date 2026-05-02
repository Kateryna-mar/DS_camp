import pandas as pd
VALID_STATUSES = ["pending", "shipped", "delivered", "cancelled"]

def clean_customers(df):
    df = df.drop_duplicates(subset="customer_id")
    df = df[df["customer_id"].notna()]
    df = df[df["email"].str.contains("@", na=False)]
    df["email"] = df["email"].str.lower()
    return df


def clean_products(df):
    df = df.drop_duplicates(subset="product_id")
    df = df[df["price"] > 0]
    return df


VALID_STATUSES = ["pending", "shipped", "delivered", "cancelled"]

def clean_orders(df):
    df = df.drop_duplicates(subset="order_id")

    df["order_status"] = df["order_status"].str.lower()

    df = df[df["order_status"].isin(VALID_STATUSES)].copy()
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    df = df[df["created_at"].notna()]

    return df


def clean_order_items(df, products, orders):
    df = df.drop_duplicates()
    df = df[df["quantity"] > 0]
    df = df[df["order_id"].isin(orders["order_id"])]
    df = df[df["product_id"].isin(products["product_id"])]
    return df