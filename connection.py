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
        CREATE TABLE IF NOT EXISTS users(
            user_id serial primary key,
            username varchar(50) not null,
            full_name varchar(50),
            age smallint,
            password_hash varchar,
            created_at timestamp default now(),
            is_active boolean default true
        );
         
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS dishes (
            dish_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            category_id INT REFERENCES categories(category_id)
        );

        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            dish_id INT REFERENCES dishes(dish_id),
            user_id INT REFERENCES users(user_id),
            quantity INT NOT NULL,
            total_price NUMERIC(10, 2) NOT NULL
        );
        """)
    except Exception as error:
        print("Error in creating tables: ",error)
    finally:
      await conn.close()