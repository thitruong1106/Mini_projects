"""
Purpose: Build a CLI to store, search, list and delete contacts in a JSON file. 
"""
import json
import os 

CONTACT_FILE = "contacts.json"

#Helper function 

def load_contacts():
    if os.path.exists(CONTACT_FILE): #If file exisit 
        with open(CONTACT_FILE, 'r', newline="", encoding="utf-8") as f: #Read 
            return json.load(f)
        #handle cases where file is empty 
        return []
    #Return Empty list if file doesnt exists 
    return []
    
def save_contacts(contacts):
    #Save a new contact 
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4) #dump contact to file

def view_contacts(contacts): 
    #view all saved contacts 
    if not contacts:
        print("\n No contacts Found")
        return
    print("\n Contact List:")
    for idx, contact in enumerate (contacts, start=1):
        print(f"{idx}, {contact['name']} - {contact['phone']} - {contact['email']}")
        print()

def add_contacts(contacts):
    "Add new entry into json file"
    name = input("Enter the name: \t").strip()
    phone = input("Enter a phone number: \t").strip()
    email = input("Enter an email: \t").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully.")

def search_contact(contacts):
    "Search contact by keyword NAME"
    keyword = input("Enter a name to search: \n").strip().lower()
    results = [c for c in contacts if keyword in c['name'].lower()]
    if results: 
        print("\nSearch Results:")
        for c in results:
            print(f"- {c['name']} | {c['phone']} | {c['email']}")
        else:
            print("No contact has been found")

def delete_contacts(contacts):
    "Delete by name"
    name = input("Enter the name of the contact to be deleted: \t").strip()
    for c in contacts: 
        if c['name'].lower() == name.lower(): #if contact name matches input
            contacts.remove(c)
            save_contacts(contacts)
            print(f"{name} contact has been removed succesfully.")
            return 
        print("Contact is not Found.")

def main():
    contact = load_contacts()
    while True:
        print("Welcome to Contact Book")
        print("1. Load Contact")
        print("2. Add contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose option (1 - 5)")
        if choice == "1":
            view_contacts(contact)
        elif choice == "2":
            add_contacts(contact)
        elif choice == "3":
            search_contact(contact)
        elif choice == "4":
            delete_contacts(contact)
        elif choice == "5":
            break
        else:
            print("Invalid input, Enter a valid choice (1 - 5)")

if __name__ == "__main__":
    main()