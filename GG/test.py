import os
import shutil
def rename_images(folder_path, new_prefix,i):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for filename in file_list:
        # Check if the file is an image (optional)
        if not filename.endswith(('.jpg', '.jpeg', '.png')):
            continue

        # Change the image name
        new_name = f"{filename}_{folder_path}.jpg"
        image_path = os.path.join(folder_path, filename)
        new_image_path = os.path.join(folder_path, new_name)
        i=i+1

        # Rename the file
        os.rename(image_path, new_image_path)

        print(f"Renamed {filename} to {new_name}")

# Example usage
# i=100
# folder_path = "ruiSuGHJf6Q_005729"  # Replace with your folder path
# new_prefix = "new_image"  # Replace with your desired prefix
# rename_images(folder_path, new_prefix,i)

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

def write_folder_names_to_memo(item, memo_file):
    # Get a list of all items in the directory

    # Open the memo file in append mode
    with open(memo_file, "a") as f:
        # Iterate over each item
        f.write(item + "\n")


image_sequence = 0
print(str(image_sequence).zfill(6))

directory = "/Users/박주성/Desktop/test_data/sample/GG"  # Replace with the directory path
memo_file = "/Users/박주성/Desktop/test_data/sample/GG/test.txt"  # Replace with the path to the memo file
target_folder="/Users/박주성/Desktop/test_data/sample/GG/sum_image"  # Replace with the directory path

items = os.listdir(directory)
for item in items:
    item_path = os.path.join(directory, item)
    if os.path.isdir(item_path):
        if item_path=="sum_image":
            continue
        # print(item)
        # write_folder_names_to_memo(item, memo_file)
        file_list = os.listdir(item_path)
        for file_name in file_list:
            if not file_name.endswith(('.jpg', '.jpeg', '.png')):
                continue
            image_sequence = image_sequence + 1
            new_name = str(image_sequence).zfill(6) + ".jpg"
            image_path = os.path.join(item_path, file_name)
            new_image_path = os.path.join(item_path, new_name)
            os.rename(image_path, new_image_path)
            print(f"Renamed {file_name} to {new_name}")
            shutil.move(new_image_path, target_folder)

