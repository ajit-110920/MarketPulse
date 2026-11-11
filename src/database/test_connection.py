from sqlalchemy import text
from src.database.connection import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT version()"))
    print(result.scalar())

print("Database connected successfully!")