"""
Features:

Ask for item name + price.

Save each entry to a text file or CSV.

When user types report, print total items + total spent.

Type q to quit.
"""
import os, csv 
from datetime import datetime, timedelta

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

def get_report_period():
    print("\nView report for:")
    print("1. Today")
    print("2. This week")
    print("3. All time")
    period = input("Choose option (1-3): ").strip()
    return period 

def generate_report(path, period_choice):
    if not os.path.exists(path):
        print("No expense record yet")
        return
    
    total_cost = 0 
    count = 0 

    with open(path, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")

            item_cost = float(row["Cost"])
            #Filter based on date choice 
            if period_choice == "1": #Today
                if timestamp.date() == datetime.now().date():
                    count += 1
                    total_cost += item_cost
            elif period_choice == "2": #This Week
                week_start = datetime.now() - timedelta(days=datetime.now().weekday())
                if timestamp >= week_start.replace(hour=0, minute=0, second=0, microsecond=0):
                    count += 1 
                    total_cost += item_cost
                elif period_choice == "3":
                    count += 1 
                    total_cost += item_cost
    #display results based on period 
    period_names = {"1" : "Today", "2":"This Week", "3": "All Time"}
    period_name = period_names.get(period_choice, "all time")

    print(f"Report for {period_name}:")
    print(f"Items: {count}")
    print(f"Total Cost: {total_cost}")

path = "expense.csv"
while True:
    display_menu()
    choice = input("").strip().lower()
    if choice == "1":
        item = input("Enter item name").strip().lower()
        try:
            cost = float(input("Enter cost amount"))
            if cost <0:
                print("Cost cannot be negative")
                continue
        except ValueError:
            print("Enter enter a float amount or int")
            continue
        #Create timestamp 
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        header_once(path, ["Timestamp", "Item", "Cost"])
        write_row(path, [timestamp, item, cost])
        print(f"Added {item}: {cost} to {path}")

    elif choice == "2":
        period_choice = get_report_period() #print menu and return choice select 
        if period_choice in ["1", "2", "3"]: #If choice is valid 
            generate_report(path, period_choice)
        else:
            print("Invalid Input")
    #q to quit 
    elif choice == 'q':
        print("Program ended")
        break
    #invalid choice 
    else:
        print("Please Enter a valid Choice")
    