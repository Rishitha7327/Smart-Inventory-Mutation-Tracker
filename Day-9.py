import copy

def create_inventory():
    return [
        {
            "item" : "Laptop",
            "details" : {
                "price" : 50000,
                "stock" : 10,
                "supplier" : {"name" :"Dell" , "rating" : 4.5}
            }
        },
        {
            "item" : "Phone",
            "details" : {
                "price" : 20000,
                "stock" : 25,
                "supplier" : {"name" :"Samsung" , "rating" : 4.2}
            }
        }
    ]

def apply_discount(data,roll_number):
    n = len(data)
    index_to_modify = roll_number % n

    for i in range(n):
        data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)

        if  i == index_to_modify:
            data[i]["details"]["stock"] -= 5
            data[i]["details"]["supplier"]["rating"] += 0.1


def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1

    return changed, unchanged



roll_number = int(input("Enter your roll number: "))

original_inventory = create_inventory()

original_backup = copy.deepcopy(original_inventory)
shallow_copy_inventory = original_inventory.copy()
deep_copy_inventory = copy.deepcopy(original_inventory)
apply_discount(shallow_copy_inventory, roll_number)
apply_discount(deep_copy_inventory, roll_number)

print("\n=== Original Inventory ===")
for item in original_inventory:
    print(item)

print("\n=== Shallow Copy Inventory ===")
for item in shallow_copy_inventory:
    print(item)

print("\n=== Deep Copy Inventory ===")
for item in deep_copy_inventory:
    print(item)

shallow_diff = compare_data(original_backup, shallow_copy_inventory)
deep_diff = compare_data(original_backup, deep_copy_inventory)

print("\n==== differences observed ====")
print("Shallow Copy ->" ,shallow_diff)
print("Deep Copy ->" ,deep_diff)

print("\n=== Explanation ===")
print("When I modified shallow copy, the original inventory also changed.")
print("For example, price values in original reduced after shallow copy modification.")
print("This shows both are connected internally.")
print("But in deep copy, original values did not change.")
print("So deep copy creates separate data and works independently.")

