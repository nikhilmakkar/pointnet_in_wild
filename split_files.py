import os

# Function to split data into chunks of size n
def chunk_data(data, n):
    return [data[i:i+n] for i in range(0, len(data), n)]

# Path to the original text file and the label file
original_file_path = "shapenetcore_partanno_segmentation_benchmark_v0/00000000/points/test.pts"
labels_file_path = "shapenetcore_partanno_segmentation_benchmark_v0/00000000/points_label/test.seg"

# Read content from the original text file and the label file
with open(original_file_path, "r") as original_file:
    data = original_file.readlines()

with open(labels_file_path, "r") as labels_file:
    labels = labels_file.readlines()

# Split data into chunks of 2500 rows each
data_chunks = chunk_data(data, 2500)
label_chunks = chunk_data(labels, 2500)

# Path to the directory where new files will be created
output_dir = "/scratch/gilbreth/makkarn/project/shapenetcore_partanno_segmentation_benchmark_v0/00000000/points"
output_dir_l = "/scratch/gilbreth/makkarn/project/shapenetcore_partanno_segmentation_benchmark_v0/00000000/points_label"
os.makedirs(output_dir, exist_ok=True)

# Write each chunk of data to a separate text file along with corresponding labels
for i, (chunk_data, chunk_labels) in enumerate(zip(data_chunks, label_chunks)):
    chunk_file_path = os.path.join(output_dir, f"test_chunk_{i}.pts")
    labels_file_path = os.path.join(output_dir_l, f"test_chunk_{i}.seg")

    with open(chunk_file_path, "w") as chunk_file:
        chunk_file.writelines(chunk_data)

    with open(labels_file_path, "w") as labels_file:
        labels_file.writelines(chunk_labels)

    print(f"Chunk {i} data has been written to {chunk_file_path}")
    print(f"Chunk {i} labels have been written to {labels_file_path}")
