Extracting intensity values for gray matter
###########################################

.. code::

   sct_extract_metric -i t2s.nii.gz -f t2s_wmseg.nii.gz -method bin -z 2:12 -o t2s_value.csv

.. code::

   sct_extract_metric -i t2s.nii.gz -f t2s_gmseg.nii.gz -method bin -z 2:12 -o t2s_value.csv -append 1

