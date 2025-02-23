import os
import uuid
import json
import subprocess

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
            folder_path = "_root"
        
        # Format the key as "folder > subfolder"
        folder_key = folder_path.replace(os.sep, ' > ')

        # Prepare the list of files in the folder
        file_details = []
        file_no = 1
        for file in files:
            file_details.append({
                "id": str(file_no),
                "name": file[:-4]
            })
            file_no = file_no + 1
        
        # Store the folder's id and list of files
        directory_structure[folder_key] = {
            "id": folder_id,
            "files": file_details
        }

        folder_no = folder_no + 1

    return directory_structure

def search_directory(base_dir, grep_str):
    # This will hold the final directory structure in the desired format
    directory_structure = {}
    folder_no = 1

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        # Skip empty directories
        if not files:
            continue

        folder_id = str(folder_no)
        folder_path = os.path.relpath(root, base_dir)
         
        # If the directory is the root directory, just add the folder name
        if folder_path == ".":
            folder_path = "_root"
            
        # Format the key as "folder > subfolder"
        folder_key = folder_path.replace(os.sep, ' > ')
          
        if grep_str in folder_path:
          # Prepare the list of files in the folder
          file_details = []
          file_no = 1
          for file in files:
              file_details.append({
                  "id": str(file_no),
                  "name": file[:-4]
              })
              file_no = file_no + 1
              
          # Store the folder's id and list of files
          directory_structure[folder_key] = {
              "id": folder_id,
              "files": file_details
          }
        else:
            matched_files=[]
            for file in files:
                if grep_str in file:
                  file_details.append({
                      "id": str(file_no),
                      "name": file[:-4]
                  })
                  file_no = file_no + 1

        folder_no = folder_no + 1

    return directory_structure


def passage_execute(commands):
    result = subprocess.run(commands, capture_output=True, text=True)
    if (result.returncode != 0 or result.stderr):
        return null
    else:
        return result.stdout.strip()

def passage_exitstatus(commands):
    return subprocess.call(commands)

def passage_new(password, path):
    try:
        # Create a pipe from echo to passage insert
        echo_process = subprocess.Popen(
            ["echo", password], 
            stdout=subprocess.PIPE  # Send output to pipe
        )

        # Pass the output of echo to passage insert
        passage_process = subprocess.Popen(
            ["passage", "insert", "-e", path],
            stdin=echo_process.stdout,  # Receive input from the echo command's stdout
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait for the command to finish and capture the output and error
        output, error = passage_process.communicate()

        # Check if there is any error
        if error:
            print(f"Error occurred: {error.decode()}")
        else:
            print(f"Output: {output.decode()}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
