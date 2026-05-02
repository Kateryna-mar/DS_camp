import pandas as pd

def load_raw_data(path="data/raw"):
    return {
        "customers": pd.read_csv(f"data/raw/customers.csv"),
        "products": pd.read_csv(f"data/raw/products.csv"),
        "orders": pd.read_csv(f"data/raw/orders.csv"),
        "order_items": pd.read_csv(f"data/raw/order_items.csv"),
    }