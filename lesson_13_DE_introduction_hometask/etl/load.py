from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://etl_user:etl_pass@localhost:5432/etl_db"
)

def load_table(df, table_name):
    df.to_sql(table_name, engine, if_exists="replace", index=False)