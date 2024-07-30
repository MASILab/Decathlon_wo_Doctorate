#spleensplit

import os
import shutil
import random

def copy_and_split_images(input_dir, output_dir, train_ratio=0.8):
    # Create output directories if they don't exist
    altrain_dir = os.path.join(output_dir, 'ALtrain')
    edutrain_dir = os.path.join(output_dir, 'Edutrain')
    os.makedirs(altrain_dir, exist_ok=True)
    os.makedirs(edutrain_dir, exist_ok=True)
    
    # Get all files in the input directory
    all_files = [f for f in os.listdir(input_dir) if f.endswith('.nii') or f.endswith('.nii.gz')]
    
    # Randomly shuffle the files
    random.shuffle(all_files)
    
    # Calculate split point
    split_point = int(len(all_files) * train_ratio)
    
    # Split files into ALtrain and Edutrain
    altrain_files = all_files[:split_point]
    edutrain_files = all_files[split_point:]
    
    # Copy files to the corresponding directories
    for f in altrain_files:
        shutil.copy(os.path.join(input_dir, f), os.path.join(altrain_dir, f))
    
    for f in edutrain_files:
        shutil.copy(os.path.join(input_dir, f), os.path.join(edutrain_dir, f))
    
    print(f"Copied {len(altrain_files)} files to {altrain_dir}")
    print(f"Copied {len(edutrain_files)} files to {edutrain_dir}")
    
    return altrain_files, edutrain_files

def copy_labels(images_list, labels_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    
    for image_file in images_list:
        label_file = image_file  # Assuming the label file name matches the image file name
        src_label_path = os.path.join(labels_dir, label_file)
        if os.path.exists(src_label_path):
            shutil.copy(src_label_path, os.path.join(target_dir, label_file))
        else:
            print(f"Label file for {image_file} not found in {labels_dir}")

def main():
    images_input_dir = '/home-local/samirj/datasets/Task09_Spleen/imagesTr'
    labels_input_dir = '/home-local/samirj/datasets/Task09_Spleen/labelsTr'
    output_directory = '/home-local/samirj/datasets/Task09_Spleen'
    
    # Split and copy images
    altrain_files, edutrain_files = copy_and_split_images(images_input_dir, output_directory)
    
    # Copy corresponding labels
    copy_labels(altrain_files, labels_input_dir, os.path.join(output_directory, 'labelsALtrain'))
    copy_labels(edutrain_files, labels_input_dir, os.path.join(output_directory, 'labelsEdutrain'))

if __name__ == "__main__":
    main()
