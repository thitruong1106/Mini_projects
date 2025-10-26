"""
Features:

Ask for item name + price.

Save each entry to a text file or CSV.

When user types report, print total items + total spent.

Type q to quit.
"""
import os, csv 
def header_once(path, header):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)

def write_row(path,row):
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer =  csv.writer(f)
        writer.writerow(row)

def display_menu():
    
    print("1.Enter item and cost")
    print("2.View report")
    print("q to quit program")
path = "expense.csv"
while True:
    display_menu()
    choice = input("").strip().lower()
    if choice == "1":
        item = input("Enter item name").strip().lower()
        try:
            if cost <0:
                print("Cost cannot be negative")
                continue
            cost = float(input("Enter cost amount"))
        except ValueError:
            print("Enter enter a float amount or int")
            continue
        header_once(path, ["Item", "Cost"])
        write_row(path, [item, cost])
        print(f"Added {item}: {cost} to {path}")
    elif choice == "2":
        total_cost = 0
        count = 0
        with open(path, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                count += 1 
                total_cost += float(row["Cost"])
        print(f"Items: {count} \t💰 Total cost spend is {total_cost}")
    elif choice.lower() == "q":
        break
    else:
        print("Enter a valid choice")

    