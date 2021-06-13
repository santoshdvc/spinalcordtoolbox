Preprocessing steps to highlight the spinal cord
################################################

.. code::

   sct_maths -i dmri.nii.gz -mean t -o dmri_mean.nii.gz

.. code::

   sct_propseg -i dmri_mean.nii.gz -c dwi -qc ~/qc_singleSubj

.. code::

   sct_create_mask -i dmri_mean.nii.gz -p centerline,dmri_mean_seg.nii.gz -size 35mm

.. code::

   sct_crop_image -i dmri.nii.gz -m mask_dmri_mean.nii.gz -o dmri_crop.nii.gz