#overlayfigures

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

def load_nifti_image(file_path):
    img = nib.load(file_path)
    return img.get_fdata()

def overlay_images(ct_scan, expert_label, novice_label):
    # Assume all images are of the same shape
    overlay = np.zeros((*ct_scan.shape, 3))  # Create an empty 3-channel image

    # Scaling ct_scan intensity to [0, 1] for visualization
    scaled_ct_scan = (ct_scan - np.min(ct_scan)) / (np.max(ct_scan) - np.min(ct_scan))

    # Fill grayscale channel
    for i in range(3):
        overlay[..., i] = scaled_ct_scan

    # Apply red (novice) and blue (expert) overlays where labels are present
    overlay[novice_label > 0, 0] = 1    # Red channel for novice
    overlay[expert_label > 0, 2] = 1    # Blue channel for expert
    
    return overlay

def main():
    ct_scan_path = '/home-local/samirj/datasets/Task09_Spleen/ALtrain/spleen_16.nii.gz'
    expert_label_path = '/home-local/samirj/datasets/Task09_Spleen/labelsALtrain/spleen_16.nii.gz'
    novice_label_path = '/home-local/samirj/datasets/Task09_Spleen/ALtrain/labels/final/spleen_16.nii.gz'

    ct_scan = load_nifti_image(ct_scan_path)
    expert_label = load_nifti_image(expert_label_path)
    novice_label = load_nifti_image(novice_label_path)

    overlay_image = overlay_images(ct_scan, expert_label, novice_label)

    # Ask user for the slice number
    slice_idx = int(input(f"Enter the slice number to view (0 to {ct_scan.shape[2]-1}): "))

    # Ensure the slice index is within bounds
    slice_idx = max(0, min(slice_idx, ct_scan.shape[2] - 1))

    plt.imshow(overlay_image[:, :, slice_idx])
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()


