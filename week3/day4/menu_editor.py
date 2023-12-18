from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Program Menu:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")


def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))

    item = MenuItem(name, price)
    item.save()
    print("Item added successfully.")


def remove_item_from_menu():
    name = input("Enter item name to remove: ")

    item = MenuItem(name, 0)  
    item.delete()
    print(f"Item '{name}' deleted successfully.")


def update_item_from_menu():
    old_name = input("Enter item name to update: ")
    old_price = int(input("Enter current item price: "))
    new_name = input("Enter new item name: ")
    new_price = int(input("Enter new item price: "))

    item = MenuItem(old_name, old_price)
    item.update(new_name, new_price)
    print(f"Item '{old_name}' updated successfully.")


def show_restaurant_menu():
    items = MenuManager.all_items()
    print("Restaurant Menu:")
    for item in items:
        print(f"{item[1]} - ${item[2]}")


def main():
    while True:
        show_user_menu()
        choice = input("Enter your choice (V/A/D/U/S/E): ").upper()

        if choice == 'V':
            name_to_view = input("Enter item name to view: ")
            item = MenuManager.get_by_name(name_to_view)
            print(item if item else "Item not found.")

        elif choice == 'A':
            add_item_to_menu()

        elif choice == 'D':
            remove_item_from_menu()

        elif choice == 'U':
            update_item_from_menu()

        elif choice == 'S':
            show_restaurant_menu()

        elif choice == 'E':
            show_restaurant_menu()
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter V, A, D, U, S, or E.")


if __name__ == "__main__":
    main()
