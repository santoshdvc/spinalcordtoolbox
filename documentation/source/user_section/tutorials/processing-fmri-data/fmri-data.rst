Working with fMRI data
######################

.. code::

   sct_maths -i fmri.nii.gz -mean t -o fmri_mean.nii.gz

.. code::

   sct_register_multimodal -i ../t2/t2_seg.nii.gz -d fmri_mean.nii.gz -identity 1

.. code::

   sct_create_mask -i fmri.nii.gz -p centerline,t2_seg_reg.nii.gz -size 35mm -f cylinder

.. code::

   sct_fmri_moco -i fmri.nii.gz -m mask_fmri.nii.gz

.. code::

   sct_register_multimodal -i $SCT_DIR/data/PAM50/template/PAM50_t2s.nii.gz -d fmri_moco_mean.nii.gz -dseg t2_seg_reg.nii.gz -param step=1,type=im,algo=syn,metric=CC,iter=5,slicewise=0 -initwarp ../t2s/warp_template2t2s.nii.gz -initwarpinv ../t2s/warp_t2s2template.nii.gz -qc ~/qc_singleSubj

.. code::

   mv warp_PAM50_t2s2fmri_moco_mean.nii.gz warp_template2fmri.nii.gz && mv warp_fmri_moco_mean2PAM50_t2s.nii.gz warp_fmri2template.nii.gz

.. code::

   sct_warp_template -d fmri_moco_mean.nii.gz -w warp_template2fmri.nii.gz -s 1 -a 0
