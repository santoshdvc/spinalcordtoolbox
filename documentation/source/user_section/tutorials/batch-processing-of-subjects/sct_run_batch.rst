sct_run_batch
#############

.. code::

   # Go to the multi_subject folder
   cd ../../../multi_subject

.. code::

   # set proper permissions
   chmod 775 *

.. code::

   # If needed, edit parameters.sh according to your config.
   # Process data (takes 10-30 min). While data are being processed you can follow the QC report
   sct_run_batch parameters.sh process_data.sh