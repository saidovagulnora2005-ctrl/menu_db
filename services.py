from connection import get_connection



async def add_category(name):
    conn = await get_connection()
    await conn.execute(
        "INSERT INTO categories(name) VALUES($1)",name)
    await conn.close()
    print("Category added!")


async def show_categories():
    conn = await get_connection()
    rows = await conn.fetch(
        "SELECT * FROM categories ORDER BY category_id")
    await conn.close()
    for row in rows:
        print(row["category_id"], row["name"])


async def update_category(category_id, name):
    conn = await get_connection()
    await conn.execute(
        "UPDATE categories SET name=$1 WHERE category_id=$2",name, category_id)
    await conn.close()
    print("Category updated!")


async def delete_category(category_id):
    conn = await get_connection()
    await conn.execute(
        "DELETE FROM categories WHERE category_id=$1",category_id)
    await conn.close()
    print("Category deleted!")


async def add_dish(name, price, category_id):
    conn = await get_connection()
    await conn.execute("""
        INSERT INTO dishes(name, price, category_id) VALUES($1, $2, $3)
        """,name, price, category_id)
    await conn.close()
    print("Dish added!")


async def show_dishes():
    conn = await get_connection()
    rows = await conn.fetch("""
        SELECT dishes.dish_id,dishes.name,dishes.price,categories.name AS category FROM dishes LEFT JOIN categories 
        ON dishes.category_id = categories.category_id ORDER BY dishes.dish_id
    """)
    await conn.close()
    for row in rows:
        print(row["dish_id"],row["name"],row["price"],"-",row["category"])


async def update_dish(dish_id, name, price, category_id):
    conn = await get_connection()
    await conn.execute("""
        UPDATE dishes SET name=$1, price=$2, category_id=$3 WHERE dish_id=$4
        """,name, price, category_id, dish_id)
    await conn.close()
    print("Dish updated!")


async def delete_dish(dish_id):
    conn = await get_connection()
    await conn.execute(
        "DELETE FROM dishes WHERE dish_id=$1",dish_id)
    await conn.close()
    print("Dish deleted!")


async def add_order(dish_id, quantity):
    conn = await get_connection()
    dish = await conn.fetchrow(
        "SELECT price FROM dishes WHERE dish_id=$1",dish_id)
    if dish is None:
        print("Dish not found!")
        await conn.close()
        return

    total_price = dish["price"] * quantity
    await conn.execute(
        """
        INSERT INTO orders(dish_id, quantity, total_price) VALUES($1, $2, $3)
        """,dish_id, quantity, total_price)
    await conn.close()
    print("Order added!")
    print("Total price:", total_price)


async def show_orders():
    conn = await get_connection()
    rows = await conn.fetch("""
        SELECT orders.order_id, dishes.name,orders.quantity,orders.total_price FROM orders
        JOIN dishes ON orders.dish_id = dishes.dish_id ORDER BY orders.order_id
        """)
    await conn.close()
    for row in rows:
        print("Order:",row["order_id"],"| Dish:",row["name"],"| Quantity:",row["quantity"],"| Total:",row["total_price"])


async def update_order(order_id, dish_id, quantity):
    conn = await get_connection()
    dish = await conn.fetchrow(
        "SELECT price FROM dishes WHERE dish_id=$1",dish_id)
    if dish is None:
        print("Dish not found!")
        await conn.close()
        return
    total_price = dish["price"] * quantity
    await conn.execute("""
        UPDATE orders SET dish_id = $1, quantity = $2,total_price = $3 WHERE order_id = $4
        """,dish_id,quantity,total_price,order_id)
    await conn.close()
    print("Order updated!")


async def delete_order(order_id):
    conn = await get_connection()
    await conn.execute(
        "DELETE FROM orders WHERE order_id = $1",order_id)
    await conn.close()
    print("Order deleted!")