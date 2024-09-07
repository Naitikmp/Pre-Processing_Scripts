# -------------------------Made code-------------------------------------
import json
import os

#Define the category mapping and the categories to remove
#Mapping to merge or standardize categories
label_mapping = {
    # 'add-on;LPS;OK': 'Add-on OK',
    # 'add-on;serration;OK': 'Add-on OK',
    # 'add-on;markings;CoG': 'Add-on Markings',
    # 'add-on;LPS;other' :'Add-on OK',
    # 'add-on;markings;lifting point' : 'Add-on Markings',
    # 'add-on;VG;OK' : 'Add-on OK',
    # 'add-on;dynotail;OK' : 'Add-on OK',
    # 'add-on;markings;text' : 'Add-on OK',
    # 'Surface;contamination;dirt': 'Surface Contamination',
    # 'add-on;drainhole;OK' : 'Add-on OK',
    # 'add-on;tip;OK': 'Add-on OK',
    # 'surface;contamination;other': 'Surface Contamination',
    # ---------------------------------
    # 'Oil Leakage': 'Oil Leakage',
    # 'add-on;LPS;worn or burnt' : 'LPS burnt',
    # 'Paint Peel Off': 'Paint Peel Off',
    # 'LE-Erosion': 'LE-Erosion',
    # 'leading edge;erosion;coating or LEP only': 'LE-Erosion',
    # 'leading edge;erosion;eroded tip': 'LE-Erosion',
    # 'leading edge;erosion;continuous or deep': 'LE-Erosion',
    # 'leading edge;erosion;spotty or laminate': 'LE-Erosion',
    # 'surface;crack or laminate defect;superficial' : 'Surface Damage',
    # 'surface;coating damage;superficial': 'Surface Damage',
    # 'surface;burn damage;superficial': 'Surface Damage',
    # 'surface;burn damage;deep': 'Surface Damage',
    # 'trailing edge;crack;deep': 'Crack',
    # 'trailing edge;crack;superficial': 'Crack',
    # 'Lighting-Strike': 'Lightning-Strike',
    # 'LE LAMINATE DAMAGE' : 'LE-Erosion',
    # 'PU TAPE DAMAGE' : 'LE-Erosion',
    # 'OIL LEAKAGE' : 'Oil Leakage',
    # 'PAINT DAMAGE' : 'Paint Peel Off',
    # 'Surface Crack' : 'Crack',
    # 'LE-Erosion' : 'LE-Erosion',
    # 'Paint Peel Off' : 'Paint Peel Off',
    # 'PU Tape Damage' : 'LE-Erosion',
    # 'Lightning Strike' : 'Lightning-Strike',
    # 'DH Oil Leakage' : 'Oil Leakage',
    'PAINT-DEMAGE' : 'Paint Peel Off',
    'Paint Peel Off' : 'Paint Peel Off',
    'Lightning-Strike' : 'Lightning-Strike',
    'PU-TAPE-DEMAGE' : 'LE-Erosion',
    'LE-Erosion' : 'LE-Erosion',
    'OIL-LEAKS' : 'Oil Leakage',
    'Oil Leakage' : 'Oil Leakage'
    
}

labels_to_remove = {
    # 'add-on;LPS;OK',
    # 'add-on;serration;OK',
    # 'add-on;markings;CoG',
    # 'add-on;LPS;other' ,
    # 'add-on;markings;lifting point',
    # 'add-on;VG;OK',
    # 'add-on;dynotail;OK',
    # 'add-on;markings;text',
    # 'Surface;contamination;dirt',
    # 'add-on;drainhole;OK',
    # 'add-on;tip;OK',
    # 'surface;contamination;other'
    # 'Stickers',
    # 'Bolts'
    # 'Pressure Side-2',
    # 'Leading side-3',
    # 'Leading side-1',
    # 'suction side-2',
    # 'Leading side-2',
    # 'Pressure Side-1',
    # 'suction side-1',
    # 'Pressure Side-3',
    # 'suction side-3',
    # 'Drain hole impairment',
    # 'Dirt',
    'DUST',
    'VG-Panel',
    'VG-Panel-With-Missing-Teeth' 

}
# Function to get all the json files from the root directory and update them
def loadAllJSONfiles(root_dir):
    for sub_dir,_,files in os.walk(root_dir):
        for file in files :
            if file.endswith('json'):
                json_path=os.path.join(sub_dir,file)
                with open(json_path,'r') as f:
                    data = json.load(f)
                    # Get the labels from the JSON
                    shapes = data.get('shapes',[])
                    #Use a list comprehension to filter out shapes with labels in labels_to_remove
                    filtered_shapes = [shape for shape in shapes if shape.get('label') not in labels_to_remove]
                    for shape in filtered_shapes:
                      old_label = shape.get('label')
                      # Update the label if its in the label_mapping 
                      shape['label'] = label_mapping[old_label]
                    # Update the 'shapes' in data with the modified filtered_shapes
                    data['shapes'] = filtered_shapes
                # Construct the new file path with 'updated_' prefix
                # new_file_name = f"updated_{file}"
                # new_json_path = os.path.join(sub_dir, new_file_name)
            
                # Save the updated data to the new JSON path
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)  # Using indent=4 for pretty-printing
                    print("updated annotations for the file : ",file)             

def main():
    # Your main code logic here
    root_dir = 'path towards your root directory'
    loadAllJSONfiles(root_dir)
if __name__ == "__main__":
    main()
