import json
import os

def load_coco_annotations_from_multiple_files(root_dir):
    # This function will load all COCO annotations from JSON files in the given root directory and subdirectories.
    coco_data = {'annotations': []}
    
    # Walk through all folders and subfolders
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(subdir, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                    for shapes in  data.get('shapes'):
                        # print(shapes.get('label'))
                    # Combine annotations from all files
                        coco_data['annotations'].append(shapes.get('label', []))

    return coco_data

def list_non_identical_annotations(coco_data):
    # Extract all annotations
    annotations = coco_data.get('annotations', [])
    # Use a set to keep track of unique annotations
    unique_annotations = set()

    # Extract unique annotations based on their segmentation and bounding box
    for ann in annotations:
        # You can use a tuple of segmentation or bbox for uniqueness
        # print(ann.shape.label)
        # seg_key = tuple(ann.get('shapes', []))
        # bbox_key = tuple(ann.get('bbox', []))
        # annotation_key = (seg_key, bbox_key)  # Add other properties if needed

        # Add to the set to filter out duplicates
        unique_annotations.add(ann)

    return unique_annotations

# Path to the root directory containing multiple folders with JSON files
root_dir = 'path to you directory'

# Load all annotations from the multiple JSON files
coco_data = load_coco_annotations_from_multiple_files(root_dir)
# Get the list of non-identical annotations
non_identical_annotations = list_non_identical_annotations(coco_data)
for index, value in enumerate(non_identical_annotations):
    print(index, value)

# Print the results
# for i, annotation in enumerate(non_identical_annotations):
#     print(f"Annotation {i+1}: Segmentation = {annotation[0]}, Bounding Box = {annotation[1]}")
