import csv

print("=== DOG ANNOTATION TOOL ===")
print("Type 'quit' to stop\n")

# Create file with headers if it doesn't exist
with open("dogs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Dog ID", "Breed", "Color", "Size"])

while True:
    dog_id = input("Dog ID (e.g. dog_001): ")
    if dog_id == "quit":
        break

    breed = input("Breed: ")
    color = input("Color: ")
    size = input("Size (small/medium/large): ")

    # Save to CSV file
    with open("dogs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([dog_id, breed, color, size])

    print(f"\nSaved: {dog_id} | {breed} | {color} | {size}\n")
    print("--- Next Dog ---\n")

print("Done! Check dogs.csv file!")