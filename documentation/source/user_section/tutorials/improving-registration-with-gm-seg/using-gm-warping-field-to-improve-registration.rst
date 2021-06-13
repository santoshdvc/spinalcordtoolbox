Reusing the T2* warping field to improve MTI registration
#########################################################

.. code::

   cd ../mt

Performing registration to generate the warping fields
------------------------------------------------------

.. code::

   sct_register_multimodal -i $SCT_DIR/data/PAM50/template/PAM50_t2.nii.gz -iseg $SCT_DIR/data/PAM50/template/PAM50_cord.nii.gz \
                           -d mt1.nii.gz -dseg mt1_seg.nii.gz \
                           -param step=1,type=seg,algo=centermass:step=2,type=seg,algo=bsplinesyn,slicewise=1,iter=3 \
                           -m mask_mt1.nii.gz \
                           -initwarp ../t2s/warp_template2t2s.nii.gz \
                           -qc ~/qc_singleSubj

.. code::

   mv warp_PAM50_t22mt1.nii.gz warp_template2mt.nii.gz

Applying the warping field to the PAM50 template
------------------------------------------------

.. code::

   sct_warp_template -d mt1.nii.gz -w warp_template2mt.nii.gz -qc ~/qc_singleSubj