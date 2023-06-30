
inventory = []


sales_record = []

def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    snack_price = float(input("Enter snack price: "))
    snack_availability = input("Is the snack available? (yes/no): ")

    snack = {
        'id': snack_id,
        'name': snack_name,
        'price': snack_price,
        'availability': snack_availability.lower() == 'yes'
    }

    inventory.append(snack)
    print("Snack added to inventory.")

def remove_snack():
    snack_id = input("Enter snack ID to remove: ")

    for snack in inventory:
        if snack['id'] == snack_id:
            inventory.remove(snack)
            print("Snack removed from inventory.")
            return

    print("Snack not found.")

def update_snack_availability():
    snack_id = input("Enter snack ID to update availability: ")

    for snack in inventory:
        if snack['id'] == snack_id:
            new_availability = input("Is the snack available? (yes/no): ")
            snack['availability'] = new_availability.lower() == 'yes'
            print("Snack availability updated.")
            return

    print("Snack not found.")

def sell_snack():
    snack_id = input("Enter snack ID to sell: ")

    for snack in inventory:
        if snack['id'] == snack_id:
            if snack['availability']:
                sales_record.append(snack)
                inventory.remove(snack)
                print("Snack sold.")
                return
            else:
                print("Snack is unavailable.")
                return

    print("Snack not found.")

def display_inventory():
    print("Snack Inventory:")
    for snack in inventory:
        print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {'Yes' if snack['availability'] else 'No'}")

def display_sales_record():
    print("Sales Record:")
    for snack in sales_record:
        print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}")

def display_menu():
    print("Welcome to Mumbai Munchies ")
    print("1. Add the Snack")
    print("2. Remove the Snack ")
    print("3. Update the Snack Availability")
    print("4. Sell Snack")
    print("5. Display ")
    print("6. Sales record")
    print("7. Quit")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_snack()
    elif choice == '2':
        remove_snack()
    elif choice == '3':
        update_snack_availability()
    elif choice == '4':
        sell_snack()
    elif choice == '5':
        display_inventory()
    elif choice == '6':
        display_sales_record()
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")
