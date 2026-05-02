from sqlalchemy import create_engine

def get_engine():
    return create_engine(
        "postgresql://etl_user:etl_pass@localhost:5432/etl_db"
    )