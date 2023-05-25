import os

def rename_folder(old_folder_path, new_folder_name):
    # Get the parent directory of the old folder
    parent_directory = os.path.dirname(old_folder_path)

    # Construct the new folder path
    new_folder_path = os.path.join(parent_directory, new_folder_name)

    # Rename the folder
    os.rename(old_folder_path, new_folder_path)

    print(f"Folder renamed from '{old_folder_path}' to '{new_folder_path}'")

# # Example usage
# old_folder_path = "/path/to/old_folder"  # Replace with the path of the folder to be renamed
# new_folder_name = "new_folder_name"  # Replace with the desired new folder name
# rename_folder(old_folder_path, new_folder_name)

def print_folder_names(directory):
    # Get a list of all items in the directory
    items = os.listdir(directory)

    # Iterate over each item
    for item in items:
        item_path = os.path.join(directory, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            print(item)

# Example usage
directory = "/Users/박주성/Desktop/test_data/sample"  # Replace with the directory path
print_folder_names(directory)
File = open("test.txt", "w")

print("test success", file=File)
print("test success", file=File)
File.close()