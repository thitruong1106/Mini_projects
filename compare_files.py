import os

def compare_folder(source_dir, target_dir):
    #get list of folders in each dir 
    source_folder = set(next(os.walk(source_dir))[1])
    target_folder = set(next(os.walk(target_dir))[1])
    #Find which folder is missing 
    missing_in_target = source_folder - target_folder
    missing_in_source = target_folder - source_folder
    
    print(f"Folders missing in target ({target_dir}):")
    for folder in missing_in_target:
        print(folder)

    print(f"Folders missing in source ({target_dir}):")
    for folder in missing_in_source:
        print(folder)

source = ""
target = ""


compare_folder(source, target)