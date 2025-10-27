import os 
import shutil 

#Specify which folder to organise
folder_path = ""
#Dictionary mapping folder names, to file extension they should contain
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Music": [".mp3", ".wav"],
    "Document": [".pdf"],
    "Installation": [".exe"],
    "BambuA1": [".3mf"]

}
#Get List of all files / folders in folder_path
for filename in os.listdir(folder_path):
    file_path=os.path.join(folder_path,filename)
    if os.path.isdir(file_path): #Check if the current file is a folder 
        continue #Skip if it is a folder (Processing only files)
    ext = os.path.splitext(filename)[1].lower() #splits the filename into(name, [1]extension)
    for folder, extension in file_types.items(): #for folder, and extension in filetypes
        if ext in extension: #if ext matches extension 
            target_folder = os.path.join(folder_path,folder) #Create path for folder
            os.makedirs(target_folder, exist_ok=True) #create folder if its non-existance, exist_ok prevents error if folder exists
            shutil.move(file_path, os.path.join(target_folder,filename)) #Move file from original location to target 
            break 