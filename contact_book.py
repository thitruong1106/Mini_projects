"""
Purpose: Build a CLI to store, search, list and delete contacts in a JSON file. 
"""
import json,re,os

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
    found = False
    for c in contacts: 
        if c['name'].lower() == name.lower(): #if contact name matches input
            contacts.remove(c)
            save_contacts(contacts)
            print(f"{name} contact has been removed succesfully.")
            found = True 
            break
    if not found:
        print("Contact is not Found.")

def validate_name(name):
    name_re = r"^[A-Za-zÀ-ÿ]+([ '-][A-Za-zÀ-ÿ]+)*$"
    if re.match(name_re, name):
        return True
    else:
        return False
    
def validate_email(email):
    email_re = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_re, email):
        return True
    else:
        return False
    
def validate_phone(phone):
    phone_re = r'^04[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{2}$' #allow spaces / dashes 
    if re.match(phone_re, phone):
        return True
    else:
        return False

def add_contacts(contacts):
    "Add new entry into json file"
    while True:
        name = input("Enter the name: \t").strip()
        if validate_name(name):
            break
        else:
            print("Invalid name, Only use letters, spaces and hyphens")
    
    while True: 
        phone = input("Enter a phone number: \t").strip()
        if validate_phone(phone):
            break
        else:
            print("Invalid phone format. Must be 04 followed by 8 digits (AUS)")

    while True:
        email = input("Enter an email: \t").strip()
        if validate_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email addres")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def main():
    contacts = load_contacts()
    try:
        while True:
            print("Welcome to Contact Book")
            print("1. View Contact")
            print("2. Add contact")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Choose option (1 - 5)")
            if choice == "1":
                view_contacts(contacts)
            elif choice == "2":
                add_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                delete_contacts(contacts)
            elif choice == "5":
                print("Exiting.....")
                break
            else:
                print("Invalid input, Enter a valid choice (1 - 5)")
    except KeyboardInterrupt:
        print("Program has been terminated by user")

if __name__ == "__main__":
    main()