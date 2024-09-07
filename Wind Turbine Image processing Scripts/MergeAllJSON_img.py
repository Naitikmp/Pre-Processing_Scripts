import os
import shutil

# Define the root directory containing the JSON and image files
root_dir = r"path towards your root directory"

# Define the destination directory where the matched files will be copied
destination_dir = r"path to store all your Annotated files"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Supported image file extensions
image_extensions = {'.jpg', '.jpeg'}

# Iterate through all subdirectories and files in the root directory
for sub_dir, _, files in os.walk(root_dir):
    # Iterate over each file in the current directory
    for file in files:
        # Check if the file is a JSON file
        if file.endswith('.json'):
            # Get the base name of the JSON file (without extension)
            base_name = os.path.splitext(file)[0]
            print(f"Base name from JSON: {base_name}")
            
            # Check if there's an image file with the same base name and a valid extension
            matching_images = [
                img for img in files 
                if os.path.splitext(img)[0] == base_name and os.path.splitext(img)[1].lower() in image_extensions
            ]
            
            # Copy the JSON file to the destination directory
            if matching_images:
                # Copy the JSON file
                json_path = os.path.join(sub_dir, file)
                shutil.copy(json_path, destination_dir)
                print(f"Copied JSON file: {file}")
                
                # Copy each corresponding image file to the destination directory
                for img in matching_images:
                    image_path = os.path.join(sub_dir, img)
                    shutil.copy(image_path, destination_dir)
                    print(f"Copied matching image: {img}")

print("Copying completed.")
