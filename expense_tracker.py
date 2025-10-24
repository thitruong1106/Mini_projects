"""
    Features: 
        Ask for item name + price 
        save each entry to text file or csv 
        when user types report, print total items + total spent 
        type q to quit
"""
import csv
import os

def header_once(path, header):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)

def append_row(path, row):
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

# --- main program ---
path = "data.csv"
header = ["Name", "Age", "City"]

# Make sure the header exists first
header_once(path, header)

while True:
    print("\nEnter user details (or type 'q' to quit)")
    name = input("Name: ").strip()
    if name.lower() == "q":
        break
    age = input("Age: ").strip()
    city = input("City: ").strip()

    append_row(path, [name, age, city])
    print(f"✅ Added: {name}, {age}, {city}")
