#decathlonsubmission

import os
import nibabel as nib
import numpy as np

# Directories containing the NIFTI images
dir1 = '/Users/jessicasamir/Desktop/spie2024/yc/Task07_Pancreas'  # Directory with original images
dir2 = '/Users/jessicasamir/Desktop/spie2024/modelafter50Pred'  # Directory with replacement images
output_dir = '/Users/jessicasamir/Desktop/spie2024/50'  # Directory to save the modified images

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over the NIFTI files in the first directory
for filename in os.listdir(dir1):
    if filename.endswith('.nii') or filename.endswith('.nii.gz'):
        # Load the original image from the first directory
        img1_path = os.path.join(dir1, filename)
        img1 = nib.load(img1_path)

        # Create a new image with the same header but data set to zero
        zeroed_data = np.zeros(img1.shape)
        zeroed_img = nib.Nifti1Image(zeroed_data, img1.affine, img1.header)

        # Load the corresponding image from the second directory
        img2_path = os.path.join(dir2, filename)
        img2 = nib.load(img2_path)

        # Replace the zeroed array with the data from the second image
        replaced_img = nib.Nifti1Image(img2.get_fdata(), zeroed_img.affine, zeroed_img.header)
        #print(replaced_img, zeroed_img.header)

        # Save the modified image to the output directory
        output_path = os.path.join(output_dir, filename)
        nib.save(replaced_img, output_path)

        print(f"Processed and saved: {output_path}")

print("Processing complete.")
