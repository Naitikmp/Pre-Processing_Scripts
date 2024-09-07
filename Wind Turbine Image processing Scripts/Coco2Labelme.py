import os
import json

# Load the COCO JSON file
coco_json_path = r"path towards your single json file"
output_dir = r"path to the directory to store the files"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Supported image file extensions
image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

# Read the COCO JSON data
with open(coco_json_path, 'r') as f:
    coco_data = json.load(f)

# Create a lookup dictionary for images
images = {img['id']: img for img in coco_data['images']}

# Create a lookup dictionary for categories
categories = {cat['id']: cat['name'] for cat in coco_data['categories']}

# Group annotations by image_id
annotations_by_image = {}
for annotation in coco_data['annotations']:
    image_id = annotation['image_id']
    if image_id not in annotations_by_image:
        annotations_by_image[image_id] = []
    annotations_by_image[image_id].append(annotation)

# Convert each image's annotations into a LabelMe format and save as separate JSON files
for image_id, image_info in images.items():
    # Prepare the LabelMe format data
    labelme_data = {
        "version": "4.5.7",  # LabelMe version, can be adjusted if necessary
        "flags": {},
        "shapes": [],
        "imagePath": image_info['file_name'],
        "imageData": None,  # LabelMe expects base64 image data but it's optional for annotation purposes
        "imageHeight": image_info['height'],
        "imageWidth": image_info['width']
    }

    # Convert COCO annotations to LabelMe shapes
    if image_id in annotations_by_image:
        for annotation in annotations_by_image[image_id]:
            shape = {
                "label": categories[annotation['category_id']],
                "points": [],  # List of points for the polygon shape
                "group_id": None,
                "shape_type": "polygon",  # Assumed polygon; change based on your data needs
                "flags": {}
            }
            # Add the segmentation points
            if annotation['segmentation']:
                # Using the first segmentation, assuming a single polygon
                shape['points'] = [annotation['segmentation'][0][i:i+2] for i in range(0, len(annotation['segmentation'][0]), 2)]
            
            # Append the shape to the LabelMe data
            labelme_data['shapes'].append(shape)

    # Save the LabelMe JSON for each image
    output_path = os.path.join(output_dir, f"{os.path.splitext(image_info['file_name'])[0]}.json")
    with open(output_path, 'w') as outfile:
        json.dump(labelme_data, outfile, indent=4)

    print(f"Saved LabelMe JSON: {output_path}")

print("Conversion to LabelMe format completed.")
