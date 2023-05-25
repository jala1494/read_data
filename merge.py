import os

def rename_images(folder_path, new_prefix,i):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for filename in file_list:
        # Check if the file is an image (optional)
        if not filename.endswith(('.jpg', '.jpeg', '.png')):
            continue

        # Change the image name
        new_name = f"{new_prefix}_{i}.jpg"
        image_path = os.path.join(folder_path, filename)
        new_image_path = os.path.join(folder_path, new_name)
        i=i+1

        # Rename the file
        os.rename(image_path, new_image_path)

        print(f"Renamed {filename} to {new_name}")

# Example usage
i=100
folder_path = "sample\zRZ9PJguIfE_001741"  # Replace with your folder path
new_prefix = "new_image"  # Replace with your desired prefix
rename_images(folder_path, new_prefix,i)
