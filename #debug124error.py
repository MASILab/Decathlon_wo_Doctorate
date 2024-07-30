from SimpleITK import ReadImage
import glob
import os
import logging

# Set up logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Path to your directory containing NIfTI files
submit_file = '/home-local/samirj/MSD_JS_15/nah/Task08_HepaticVessel'

# List all NIfTI files in the directory
img_list = [x for x in glob.glob(os.path.join(submit_file, "*.nii.gz"))]

# Process each file
for path in img_list:
    try:
        img = ReadImage(path)
        # You can add additional processing here
        print(f"Successfully loaded {path}")
    except (ValueError, RuntimeError) as e:
        logger.warning(f"Could not load {path}. Error: {e}")



"""
import nibabel as nib
import numpy as np
from nibabel import casting
import sys

# Load the NIfTI file
file_path = sys.argv[1]
img = nib.load(file_path)

np_img = np.round(img.get_fdata()).astype(np.uint8)

#img_uint8 = casting.float_to_int(img.get_fdata(),np.uint8)
img.header.set_data_dtype(np.uint8)
new_img = nib.Nifti1Image(np_img.astype(img.get_data_dtype()), img.affine, img.header)

#print(new_img.header)

new_file_path = file_path
nib.save(new_img, new_file_path)

#saved_file = nib.load('/home-local/samirj/MSD_JS_15/nah/Task02_Heart/la_006_cp.nii.gz')
#print(saved_file.get_data_dtype())
"""
"""
# Get the data array
data = img.get_fdata()

# Rescale the data to the range 0-255 and convert to uint8
data_rescaled = np.interp(data, (data.min(), data.max()), (0, 255)).astype(np.uint8)

# Create a new NIfTI image with the rescaled data
new_img = nib.Nifti1Image(data_rescaled, img.affine, img.header)

# Save the new image
new_file_path = '/home-local/samirj/MSD_JS_15/nah/Task02_Heart/la_006.nii.gz'
nib.save(new_img, new_file_path)

print(f"Saved the converted file as {new_file_path}")
"""