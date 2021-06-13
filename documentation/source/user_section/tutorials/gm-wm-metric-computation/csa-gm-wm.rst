Computing CSA for gray and white matter
#######################################

.. code::

   sct_process_segmentation -i t2s_gmseg.nii.gz -o csa_gm.csv -angle-corr 0

.. code::

   sct_process_segmentation -i t2s_wmseg.nii.gz -o csa_wm.csv -angle-corr 0