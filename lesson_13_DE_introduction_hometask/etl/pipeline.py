from extract import load_raw_data
from transform import *
from load import load_table
from db import get_engine

def run_pipeline():
    data = load_raw_data()

    customers = clean_customers(data["customers"])
    products = clean_products(data["products"])
    orders = clean_orders(data["orders"])
    order_items = clean_order_items(
        data["order_items"], products, orders
    )

    load_table(customers, "customers_clean")
    load_table(products, "products_clean")
    load_table(orders, "orders_clean")
    load_table(order_items, "order_items_clean")

if __name__ == "__main__":
    run_pipeline()

def data_quality_checks(engine):
    import pandas as pd

    tables = ["customers_clean", "products_clean", "orders_clean", "order_items_clean"]

    for t in tables:
        df = pd.read_sql(f"SELECT COUNT(*) AS cnt FROM {t}", engine)
        print(f"{t}: {df['cnt'][0]} rows")

engine = get_engine()

data_quality_checks(engine)