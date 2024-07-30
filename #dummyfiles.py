#dummyfiles

import os
import numpy as np
import nibabel as nib

def create_dummy_labels_with_random_ones(image_dir, label_dir, file_names, num_ones=10):
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)
    
    for file_name in file_names:
        image_path = os.path.join(image_dir, file_name)
        label_path = os.path.join(label_dir, file_name)
        
        # Create a dummy label with the same dimensions as the corresponding image
        if os.path.isfile(image_path):
            try:
                img = nib.load(image_path)
                img_data = img.get_fdata()
                
                # Create a zero-filled array with the same shape
                label_data = np.zeros_like(img_data)
                
                # Insert random 1s into the label array
                for _ in range(num_ones):
                    random_index = tuple(np.random.randint(0, dim) for dim in label_data.shape)
                    label_data[random_index] = 1
                
                # Create a new NIfTI image
                label_img = nib.Nifti1Image(label_data, img.affine, img.header)
                
                # Save the dummy label
                nib.save(label_img, label_path)
                
                print(f"Created dummy label with random 1s for {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
        else:
            print(f"Image file {file_name} does not exist")

# Replace with your directories
image_directory = '/Users/jessicasamir/Downloads/sum24/imagesTs'
label_directory = '/Users/jessicasamir/Downloads/sum24/newlabels'
file_names = [f"hepaticvessel_{i:03d}.nii.gz" for i in range(1, 461)]  # Adjust as needed

create_dummy_labels_with_random_ones(image_directory, label_directory, file_names)



