#findinglabelpoints

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Load the image and label files
image_path = "/home-local/samirj/datasets/Task09_Spleen/ALtrain/spleen_40.nii.gz"
label_path = "/home-local/samirj/datasets/Task09_Spleen/ALtrain/labels/final/spleen_40.nii.gz"

image = nib.load(image_path).get_fdata()
labels = nib.load(label_path).get_fdata()

def show_slice(slice, title=""):
    plt.figure(figsize=(8, 8))
    plt.imshow(slice.T, cmap="gray", origin="lower")
    plt.title(title)
    plt.axis("off")
    plt.show()

# Display a middle slice of the image and labels
slice_index = image.shape[2] // 2
show_slice(image[:, :, slice_index], title="Image")
show_slice(labels[:, :, slice_index], title="Labels")

# Function to find coordinates of a specific label
def find_label_coordinates(labels, label_value):
    coordinates = np.argwhere(labels == label_value)
    return coordinates

# Assuming pancreas is labeled as 1 and tumor as 2 in the label file
spleen_coords = find_label_coordinates(labels, label_value=1)

print("Spleen coordinates:", spleen_coords)

# Example: Selecting a subset of coordinates for demonstration
spleen_sample_coords = spleen_coords[:2].tolist()

print("Sample spleen coordinates:", spleen_sample_coords)
#print("Sample tumor coordinates:", tumor_sample_coords)

data = {
    "image": "image.nii.gz",
    "spleen": spleen_sample_coords,
    #"tumor": tumor_sample_coords,
    "background": [],
}

print(data)



