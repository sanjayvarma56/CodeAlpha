#Task automation with python scripts
# Import os module for file and folder operations
# Import shutil module for moving files
# Store the source folder name
# Store the destination folder name
# Create the destination folder if it does not already exist
# Loop through all files present in the source folder
# Check whether the current file is a JPG file
# Create the complete path of the source file
# Create the complete path of the destination file
# Move the file from the source folder to the destination folder
# Display the name of the moved file
# Display a success message after all JPG files have been moved

import os
import shutil

source_folder = "source"
destination_folder = "destination"

# Create destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("All JPG files moved successfully!")