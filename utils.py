import os

def walk_directory(directory):
    result = {}

    for root, dirs, files in os.walk(directory):
        # Generate the folder path
        folder_path = os.path.relpath(root, directory)
        
        # If the folder is at the root level, its relative path will be just the folder name, not 'folder > subfolder'
        if folder_path == ".":
            folder_path = "_root"

        # Clean up the folder path to match the required format
        folder_key = folder_path.replace(os.sep, " > ")

        # Assign the list of files to the folder key
        result[folder_key] = files

    return result
