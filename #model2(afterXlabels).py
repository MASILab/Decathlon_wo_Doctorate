#model2(afterXlabels)

import os
import numpy as np
import torch
import nibabel as nib
import monai
from monai.config import print_config
from monai.apps.deepedit.transforms import (
    AddGuidanceSignalDeepEditd,
    AddGuidanceFromPointsDeepEditd,
    ResizeGuidanceMultipleLabelDeepEditd,
)
from monai.transforms import (
    Activationsd,
    AsDiscreted,
    EnsureChannelFirstd,
    EnsureTyped,
    LoadImaged,
    Orientationd,
    Resized,
    ScaleIntensityRanged,
    SqueezeDimd,
    ToNumpyd,
    ToTensord,
    KeepLargestConnectedComponent,
)
from monai.networks.nets import DynUNet
from monai.transforms import Resize

print_config()

# Labels
labels = {"spleen": 1,  "background": 0} #"tumor": 2,

spatial_size = [128, 128, 128]

model = DynUNet(
    spatial_dims=3,
    in_channels=len(labels) + 1,
    out_channels=len(labels),
    kernel_size=[3, 3, 3, 3, 3, 3],
    strides=[1, 2, 2, 2, 2, [2, 2, 1]],
    upsample_kernel_size=[2, 2, 2, 2, [2, 2, 1]],
    norm_name="instance",
    deep_supervision=False,
    res_block=True,
)

# Directories
image_dir = "/home-local/samirj/datasets/Task09_Spleen/imagesTs"
output_dir = "/home-local/samirj/datasets/Task09_Spleen/modelafter34Pred"
model_path = "/home/local/VANDERBILT/samirj/apps/radiology/model/deepedit_dynunet/train_01/model.pt"

# Load model
model.load_state_dict(torch.load(model_path))
model.cuda()
model.eval()

# Process each image in the directory
for image_file in os.listdir(image_dir):
    if not image_file.endswith(".nii.gz") or image_file.startswith("._"):
        continue

    image_path = os.path.join(image_dir, image_file)

    data = {
        "image": image_path,
        "spleen": [[80, 184, 67], [81, 171, 67]],  # Real label points
        "background": [],
    }
 #"tumor": [[271, 256, 43], [295, 284, 51]],  # Real label points
    # Pre Processing
    pre_transforms = [
        LoadImaged(keys="image", reader="NibabelReader", image_only=False),
        EnsureChannelFirstd(keys="image"),
        Orientationd(keys="image", axcodes="RAS"),
        ScaleIntensityRanged(keys="image", a_min=-175, a_max=250, b_min=0.0, b_max=1.0, clip=True),
        AddGuidanceFromPointsDeepEditd(ref_image="image", guidance="guidance", label_names=labels),
        Resized(keys="image", spatial_size=spatial_size, mode="area"),
        ResizeGuidanceMultipleLabelDeepEditd(guidance="guidance", ref_image="image"),
        AddGuidanceSignalDeepEditd(keys="image", guidance="guidance"),
        ToTensord(keys="image"),
    ]

    for t in pre_transforms:
        data = t(data)

    transformed_image = data["image"]
    guidance = data.get("guidance")

    # Evaluation
    inputs = data["image"][None].cuda()
    with torch.no_grad():
        outputs = model(inputs)
    outputs = outputs[0]
    data["pred"] = outputs

    # Post Processing
    post_transforms = [
        EnsureTyped(keys="pred"),
        Activationsd(keys="pred", softmax=True),
        AsDiscreted(keys="pred", argmax=True),
        SqueezeDimd(keys="pred", dim=0),
        ToNumpyd(keys="pred"),
    ]

    for t in post_transforms:
        data = t(data)

    pred_label = data["pred"].astype(np.uint8)

    # Save prediction
    original_image = nib.load(image_path)
    original_affine = original_image.affine
    original_shape = original_image.shape

    # Resize prediction to original shape
    pred_label_resized = Resize(spatial_size=original_shape, mode="nearest")(pred_label[np.newaxis])[0]

    # Convert to numpy array and set appropriate dtype
    pred_label_resized_np = pred_label_resized.numpy().astype(np.uint8)

    # Save predicted label using nibabel with original file name
    output_filename = os.path.join(output_dir, image_file)
    nib.save(nib.Nifti1Image(pred_label_resized_np, original_affine), output_filename)

    print(f"Saved prediction: {output_filename}")

