items = []

def add_item(item_name, location, status):
    item = {
        "name": item_name,
        "location": location,
        "status": status
    }
    items.append(item)
    print("Item added successfully!")

def view_items():
    if not items:
        print("No items found.")
    else:
        for item in items:
            print(item)

def search_item(name):
    for item in items:
        if item["name"].lower() == name.lower():
            print(item)
            return
    print("Item not found.")

def main():
    while True:
        print("\n--- Lost & Found Tracker ---")
        print("1. Add Lost Item")
        print("2. Add Found Item")
        print("3. View All Items")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            location = input("Enter location: ")
            add_item(name, location, "Lost")

        elif choice == "2":
            name = input("Enter item name: ")
            location = input("Enter location: ")
            add_item(name, location, "Found")

        elif choice == "3":
            view_items()

        elif choice == "4":
            name = input("Enter item name to search: ")
            search_item(name)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()