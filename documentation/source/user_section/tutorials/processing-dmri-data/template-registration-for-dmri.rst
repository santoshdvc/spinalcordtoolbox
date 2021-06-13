Registering dMRI data to the PAM50 template
###########################################

.. code::

   sct_propseg -i dmri_crop_moco_dwi_mean.nii.gz -c dwi -qc ~/qc_singleSubj

.. code::

   sct_register_multimodal -i $SCT_DIR/data/PAM50/template/PAM50_t1.nii.gz -iseg $SCT_DIR/data/PAM50/template/PAM50_cord.nii.gz -d dmri_crop_moco_dwi_mean.nii.gz -dseg dmri_crop_moco_dwi_mean_seg.nii.gz -param step=1,type=seg,algo=centermass:step=2,type=seg,algo=bsplinesyn,slicewise=1,iter=3 -initwarp ../t2s/warp_template2t2s.nii.gz -initwarpinv ../t2s/warp_t2s2template.nii.gz -qc ~/qc_singleSubj

.. code::

   mv warp_PAM50_t12dmri_crop_moco_dwi_mean.nii.gz warp_template2dmri.nii.gz && mv warp_dmri_crop_moco_dwi_mean2PAM50_t1.nii.gz warp_dmri2template.nii.gz

.. code::

   sct_warp_template -d dmri_crop_moco_dwi_mean.nii.gz -w warp_template2dmri.nii.gz -qc ~/qc_singleSubj