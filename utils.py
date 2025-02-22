import os
import uuid
import json

def walk_directory(base_dir):
    # This will hold the final directory structure in the desired format
    directory_structure = {}
    folder_no = 1

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        # Skip empty directories
        if not files:
            continue
        
        # Generate a unique ID for the folder
        folder_id = str(folder_no)

        # Get the relative folder path from the base directory
        folder_path = os.path.relpath(root, base_dir)
        
        # If the directory is the root directory, just add the folder name
        if folder_path == ".":
            folder_path = "folder"
        
        # Format the key as "folder > subfolder"
        folder_key = folder_path.replace(os.sep, ' > ')

        # Prepare the list of files in the folder
        file_details = []
        file_no = 1
        for file in files:
            file_details.append({
                "id": str(file_no),
                "name": file
            })
            file_no = file_no + 1
        
        # Store the folder's id and list of files
        directory_structure[folder_key] = {
            "id": folder_id,
            "files": file_details
        }

        folder_no = folder_no + 1

    return directory_structure
