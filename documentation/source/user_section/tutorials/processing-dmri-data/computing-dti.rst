Computing DTI for PAM50-registered dMRI data
############################################

.. code::

   sct_dmri_compute_dti -i dmri_crop_moco.nii.gz -bval bvals.txt -bvec bvecs.txt

.. code::

   sct_extract_metric -i dti_FA.nii.gz -vert 2:5 -perlevel 1 -method map -l 51 -o fa_in_wm.csv