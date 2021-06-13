Extracting MTR in white matter
##############################

.. code::

   sct_extract_metric -i mtr.nii.gz -method map -l 51 -o mtr_in_wm.csv

.. code::

   sct_extract_metric -i mtr.nii.gz -method map -l 4,5 -z 5:15 -o mtr_in_cst.csv

.. code::

   sct_extract_metric -i mtr.nii.gz -method wa -l 53 -vert 2:4 -o mtr_in_dc.csv