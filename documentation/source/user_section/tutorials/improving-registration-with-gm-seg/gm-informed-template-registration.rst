White matter-informed T2* template registration
###############################################

Performing registration to generate the warping fields
------------------------------------------------------

Coregistering the T2* data and the PAM50 template.

.. code::

   sct_register_multimodal -i $SCT_DIR/data/PAM50/template/PAM50_t2s.nii.gz -iseg $SCT_DIR/data/PAM50/template/PAM50_wm.nii.gz \
                           -d t2s.nii.gz -dseg t2s_wmseg.nii.gz \
                           -param step=1,type=seg,algo=rigid:step=2,type=seg,algo=bsplinesyn,slicewise=1,iter=3 \
                           -initwarp ../t2/warp_template2anat.nii.gz -initwarpinv ../t2/warp_anat2template.nii.gz \
                           -qc ~/qc_singleSubj

.. code::

   mv warp_PAM50_t2s2t2s.nii.gz warp_template2t2s.nii.gz && mv warp_t2s2PAM50_t2s.nii.gz warp_t2s2template.nii.gz

Applying the warping field to the PAM50 template
------------------------------------------------

Bringing the PAM50 template into the T2* space.

.. code::

   sct_warp_template -d t2s.nii.gz -w warp_template2t2s.nii.gz -qc ~/qc_singleSubj

