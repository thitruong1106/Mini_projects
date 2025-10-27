"""
The purpose of this script is to scan a given folder and categorize these files according to their extension. 
Two modes have been added(1.Dry Run, 2.execution)
    1. Dry runs allows preview of what would happen, listing where the files will go, if the program is to be executed. 
    2. Move files to organised folders
"""

import os 
import shutil 

#gloab
FOLDER_PATH = "C:/Users/testuser/Downloads"
def display_menu():
    print("Welcome to the file organiser 📂")
    print("1.Dry run \n2.Move Files \n3.Quit")

def organise_files(dry_run=True):
    #Specify which folder to organise
    folder_path = FOLDER_PATH
    #Dictionary mapping folder names, to file extension they should contain
    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Music": [".mp3", ".wav"],
        "Document": [".pdf", ".doc", ".docx", ".txt"],
        "Installation": [".exe"],
        "BambuA1": [".3mf"],
        "Zip": [".zip", ".rar"],
        "Sheets": [".csv", ".xlsx", ".xls"]
    }
    print(f"\n {'Dry Run' if dry_run else 'Executing'} - Scanning {folder_path}")
    files_processed = 0 
    files_to_move = 0
    folder_created = []

    #Get List of all files / folders in folder_path
    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path,filename)
        if os.path.isdir(file_path): #Check if the current file is a folder 
            continue #Skip if it is a folder (Processing only files)
        files_processed +=1
        ext = os.path.splitext(filename)[1].lower() #splits the filename into(name, [1]extension)
        moved = False
        for folder, extension in file_types.items(): #for folder, and extension in filetypes
            if ext in extension: #if ext matches extension 
                target_folder = os.path.join(folder_path,folder) #Create path for folder
                if dry_run: #If dry run is True 
                    print(f"{filename} -> {folder}/")
                    #if no folder exists 
                    if not os.path.exists(target_folder):
                        if target_folder not in folder_created:
                            folder_created.append(target_folder)
                else:
                    os.makedirs(target_folder, exist_ok=True) #create folder if its non-existance, exist_ok prevents error if folder exists
                    shutil.move(file_path, os.path.join(target_folder,filename)) #Move file from original location to target 
                    print(f"{filename} Moved to -> {folder}/")
                files_to_move += 1
                moved = True 
                break 
        if not moved:
            if dry_run:
                print(f"{filename} - No category founds for files")
    #display summary 
    print("Summary")
    print(f"Files scanned: {files_processed}")
    print(f"Files {'to move' if dry_run else 'moved'}: {files_to_move}")
    print(f"Folder {'to create' if dry_run else 'created'}: {len(set(folder_created))}")

    if dry_run and files_to_move == 0:
        print("No files need organisation - everything has been sorted")
    elif dry_run:
        print("This was a dry run, select option 2 to execute")
    
    input("\n Press enter to continue")

def main():
    folder_path = FOLDER_PATH
    #Error handling if path is valid 
    if not os.path.exists(folder_path):
        print(f"Error: Folder has not been found {folder_path}")
        print(f"Update the folder_path variable in code")
        return
    while True: 
        display_menu() #print menu
        try:
            choice = input("Enter your choice (1-3)").strip()
            if choice == "1":
                #dry run 
                organise_files(dry_run=True)
            elif choice == "2": #excution
                print("⚠️Do you want to proceed with moving your files⚠️")
                confirm = input("Are you sure you want to continue (y/n)?").strip().lower()
                if confirm == "y":
                    organise_files(dry_run=False) #set defualt dry_run to false to execute
                    print("Organisation completed")
                else: #in case of failure
                    print("Error has occured. Operation has not been completed")
            elif choice == "3":
                print("Thank you for using file organiser! Goodbye!")
                break
            else: #anything beside 1-3 is invalid 
                print("Invalid choice. Please enter 1, 2, or 3")
        except KeyboardInterrupt:
            print("Program has been terminated by user. Goodbye!")
            break
        except Exception as e:
            print("An error has occured")
            input("Press enter to continue")

if __name__ == "__main__":
    main()