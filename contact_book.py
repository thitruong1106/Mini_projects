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
        return []
    
def save_contacts(contacts):
    #Save a new contact 
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4) #dump contact to file

def view_contacts(contacts): 
    #view all saved contacts 
    if not contacts:
        print("\n No contacts Found")