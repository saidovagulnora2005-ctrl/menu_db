import asyncpg
import os
from dotenv import load_dotenv


load_dotenv()


async def get_connection():
    try:
        conn = await asyncpg.connect(
            database = "async_db",
            host = "localhost",
            user = "postgres",
            port = 5432,
            password = os.getenv("SQL_PASSWORD")
        )
        return conn
    except Exception as error:
        print("Connection Error: ",error)
        

async def init_table():
    conn  = await get_connection()
    try:
         await conn.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS dishes (
            dish_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            category_id INTEGER REFERENCES categories(category_id)
        );

        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            dish_id INTEGER REFERENCES dishes(dish_id),
            quantity INTEGER NOT NULL,
            total_price NUMERIC(10, 2) NOT NULL
        );
        """)
    except Exception as error:
        print("Error in creating tables: ",error)
    finally:
      await conn.close()