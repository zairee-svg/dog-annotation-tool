import csv
import os

print("=== DOG ANNOTATION TOOL ===")
print("Type 'quit' to stop\n")

# Create file with headers ONLY if it doesn't exist yet
if not os.path.exists("dogs.csv"):
    with open("dogs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Dog ID", "Breed", "Color", "Size"])

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty. Try again.")
            continue
        return value

while True:
    dog_id = get_input("Dog ID (e.g. dog_001): ")
    if dog_id == "quit":
        break

    breed = get_input("Breed: ")
    if breed == "quit":
        break

    color = get_input("Color: ")
    if color == "quit":
        break

    while True:
        size = get_input("Size (small/medium/large): ")
        if size.lower() in ["small", "medium", "large"]:
            break
        print("Please enter small, medium, or large.")

    # Save to CSV file - append, never wipe
    with open("dogs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([dog_id, breed, color, size])

    print(f"Saved dog {dog_id} | Breed: {breed} | Color: {color} | Size: {size}\n")

print("Done. All annotations saved in dogs.csv")
