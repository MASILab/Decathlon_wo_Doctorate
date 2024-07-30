#overlayinggroundtruthwithmine


import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

def load_nifti_image(filepath):
    """
    Load a NIfTI image from the specified filepath.
    """
    return nib.load(filepath).get_fdata()

def overlay_images(image1, image2, alpha=0.5):
    """
    Overlay two NIfTI images and display the result.
    
    Parameters:
    - image1: The first NIfTI image (Expert Label).
    - image2: The second NIfTI image (My Label).
    - alpha: The transparency level for the overlay image (default is 0.3).
    """
    # Ensure the images have the same shape
    assert image1.shape == image2.shape, "Images must have the same shape"
    
    # Create the figure and axis
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    
    # Display the middle slice of the images
    mid_slice = image1.shape[2] // 2
    ax[0].imshow(image1[:, :, mid_slice], cmap='gray')
    ax[0].set_title('Expert Label')
    ax[0].axis('off')
    
    ax[1].imshow(image2[:, :, mid_slice], cmap='gray')
    ax[1].set_title('My Label')
    ax[1].axis('off')
    
    ax[2].imshow(image1[:, :, mid_slice], cmap='gray')
    ax[2].imshow(image2[:, :, mid_slice], cmap='jet', alpha=alpha)
    ax[2].set_title('Overlay Result')
    ax[2].axis('off')
    
    plt.show()

# Filepaths to your NIfTI images
base_image_path = '/home-local/samirj/datasets/Task07_Pancreas/labelsTr/pancreas_299.nii.gz'
overlay_image_path = '/home-local/samirj/datasets/Task07_Pancreas/Tumor/labels/final/pancreas_299.nii.gz' 

# Load the NIfTI images
base_image = load_nifti_image(base_image_path)
overlay_image = load_nifti_image(overlay_image_path)

# Overlay the images and display the result
overlay_images(base_image, overlay_image, alpha=0.5)
