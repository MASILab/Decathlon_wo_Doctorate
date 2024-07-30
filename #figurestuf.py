#figurestuf

import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

def display_nifti_label_overlay(base_file_path, label_file_path, slice_index):
    try:
        # Load the base NIfTI image
        base_img = nib.load(base_file_path)
        base_data = base_img.get_fdata()
        
        # Load the label NIfTI image
        label_img = nib.load(label_file_path)
        label_data = label_img.get_fdata()
        
        # Ensure the base and label images have the same dimensions
        if base_data.shape != label_data.shape:
            print("Base image and label image dimensions do not match.")
            return
        
        # Check if the slice index is within the valid range
        if slice_index < 0 or slice_index >= base_data.shape[2]:
            print(f"Slice index {slice_index} is out of range. Valid range is 0 to {base_data.shape[2] - 1}.")
            return
        
        # Extract the specific slice from both the base and label data
        specific_slice_base = base_data[:, :, slice_index]
        specific_slice_label = label_data[:, :, slice_index]
        
        # Create a custom colormap for the labels
        cmap = ListedColormap(['none', 'sandybrown', 'green'])
        
        # Display the specific slice of the base image
        plt.imshow(specific_slice_base.T, cmap='gray', origin='lower')
        
        # Overlay the specific slice of the label image
        plt.imshow(specific_slice_label.T, cmap=cmap, alpha=0.5, origin='lower')
        
        # Create custom legend patches
        legend_patches = [Patch(color='sandybrown', label='Pancreas'),
                          Patch(color='green', label='Tumor')]
        
        # Add the legend to the plot
        plt.legend(handles=legend_patches, loc='upper right')
        
        plt.title(f'Overlay of Label on Base Image (Slice {slice_index})')
        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the paths to your NIfTI file
base_file_path = '/Users/jessicasamir/Desktop/spie2024/sum24/ALtrain/pancreas_078.nii.gz'
label_file_path = '/Users/jessicasamir/Desktop/spie2024/sum24/ALtrain/labels/final/pancreas_078.nii.gz'

# Specify the slice index you want to visualize
slice_index = 47

# Display the NIfTI image with the label overlay at the specified slice index
display_nifti_label_overlay(base_file_path, label_file_path, slice_index)
