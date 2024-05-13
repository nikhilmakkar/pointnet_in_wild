# import json
# data = [
#     "shape_data/00000000/val"
#         ]
# path = 'val.json'

# with open(path, "w") as json_file:
#     json.dump(data, json_file)

import os
import json

# Function to list all text files of a particular name pattern in a folder
def list_text_files(folder_path, file_prefix):
    text_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".pts") and file.startswith(file_prefix):
            text_files.append(os.path.join(folder_path, file))
    return text_files

# Folder path and file name prefix
folder_path = "/scratch/gilbreth/makkarn/project/shapenetcore_partanno_segmentation_benchmark_v0/00000000/points"
file_prefix = "test_chunk_"

# List all text files with the specified name pattern in the folder
text_files_from_folder = list_text_files(folder_path, file_prefix)

# Remove ".pts" extension from file names
# text_files_from_folder = [file[:-4] for file in text_files_from_folder]
text_files_from_folder = ['shape_data/00000000/'+file.split('/')[-1][:-4] for file in text_files_from_folder]

# Path to the JSON file
json_file_path = "test_list.json"

# Write data to JSON file
with open(json_file_path, "w") as json_file:
    json.dump(text_files_from_folder, json_file, indent=4)

print("JSON data has been written to", json_file_path)
