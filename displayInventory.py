stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}


def displayInventory(inventory):
    # your code goes here
    print("Inventory:")
    for item, quantity in inventory.items():
        print(quantity, item)
    print("Total number of items:", sum(inventory.values()))


if __name__ == "__main__":
    displayInventory(stuff)
