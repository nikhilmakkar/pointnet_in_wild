

# Folder path containing the text files
# folder_path = 

import os

def read_labels(file_path):
    """Read the labels from the text file."""
    with open(file_path, 'r') as file:
        labels = [int(line.strip()) for line in file]
    return labels

def write_labels(file_path, labels):
    """Write the labels to the text file."""
    with open(file_path, 'w') as file:
        for label in labels:
            file.write(str(label) + '\n')

# Folder path containing the text files
folder_path = '/scratch/gilbreth/makkarn/project/shapenetcore_partanno_segmentation_benchmark_v0/00000000/points_label'

# Choose the index of the row you want to modify
row_index_to_modify = 3  # For example, to modify the fourth row (0-indexed)

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Read labels from the text file
    labels = read_labels(file_path)

    # Check if the row index is within the range of the number of rows in the file
    if 0 <= row_index_to_modify < len(labels):
        # Change one label value while ensuring it remains within the range of 0 to 4
        original_value = labels[row_index_to_modify]  # Original value in the file
        new_value = (original_value + 1) % 5  # Change to the next value (cycling from 4 back to 0)

        # Modify the label value at the specified index
        labels[row_index_to_modify] = new_value

        # Write modified labels back to the text file
        write_labels(file_path, labels)
        print(f"File '{file_name}' modified and saved.")
    else:
        print(f"Row index is out of range in file '{file_name}'. No modification done.")
