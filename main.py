import asyncio
from services import *
from connection import init_table


async def main():
    await init_table()
    while True:
        print("\n========== SG MENU 📝: ==========")
        print("1. Categories")
        print("2. Dishes")
        print("3. Orders")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("\n--- Categories 📑 ---")
            print("1. Add category 📑")
            print("2. Show categories 📑")
            print("3. Update category 📑")
            print("4. Delete category 📑")

            num = input("Choose: ")
            if num == "1":
                name = input("Category name: ")
                await add_category(name)
            elif num == "2":
                await show_categories()
            elif num == "3":
                category_id = int(input("Category ID: "))
                name = input("New name: ")
                await update_category(category_id, name)
            elif num == "4":
                category_id = int(input("Category ID: "))
                await delete_category(category_id)

        elif choice == "2":

            print("\n--- Dishes 🦐🍕 ---")
            print("1. Add dish 🦐🍕")
            print("2. Show dishes 🦐🍕")
            print("3. Update dish 🦐🍕")
            print("4. Delete dish 🦐🍕")

            num = input("Choose: ")

            if num == "1":
                name = input("Dish name: ")
                price = float(input("Price: "))
                category_id = int(input("Category ID: "))
                await add_dish(name,price,category_id)
            elif num == "2":
                await show_dishes()
            elif num == "3":
                dish_id = int(input("Dish ID: "))
                name = input("New name: ")
                price = float(input("New price: "))
                category_id = int(input("Category ID: "))
                await update_dish(dish_id,name,price,category_id)
            elif num == "4":
                dish_id = int(input("Dish ID: "))
                await delete_dish(dish_id)
  
        elif choice == "3":

            print("\n--- Orders 🍽️---")
            print("1. Add order 🍽️")
            print("2. Show orders 🍽️")
            print("3. Update order 🍽️")
            print("4. Delete order 🍽️")

            num = input("Choose: ")

            if num == "1":
                dish_id = int(input("Dish ID: "))
                quantity = int(input("Quantity: "))
                await add_order(dish_id,quantity)
            elif num == "2":
                await show_orders()
            elif num == "3":
                order_id = int(input("Order ID: "))
                dish_id = int(input("New dish ID: "))
                quantity = int(input("New quantity: "))
                await update_order(order_id,dish_id,quantity)
            elif num == "4":
                order_id = int(input("Order ID: "))
                await delete_order(order_id)

        elif choice == "0":
            print("You quited the menu! Goodbye! 👋")
            break
        else:
            print("Wrong choice!")

if __name__ == "__main__":
    asyncio.run(main())