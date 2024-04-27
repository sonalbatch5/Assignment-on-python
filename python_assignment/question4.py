import os
import sys
import shutil
from datetime import datetime

def backup(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exists.")
        return

    # Check if destination directory exists
    if not os.path.exists(source_dir):
        print(f"Destination directory '{dest_dir}' does not exists.")
        return
  

    # Get list of files in source directory
    files = os.listdir(source_dir)

    # Copy files to destination directory
    for file in files:
        source_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)

        # Check if file with same name exists in destination directory
        if os.path.exists(dest_path):
            # Append timestamp to filename for uniqueness
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename, file_extension = os.path.splitext(file)
            new_filename = f"{filename}_{timestamp}{file_extension}"
            dest_path = os.path.join(dest_dir, new_filename)

        try:
            shutil.copy2(source_path, dest_path)
            print(f"File '{file}' copied to '{dest_path}'.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py source_directory destination_directory")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup(source_dir, dest_dir)