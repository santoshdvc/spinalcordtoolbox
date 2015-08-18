#!/usr/bin/env python
#########################################################################################
#
# Concatenate data. Replace "fsl_merge"
#
# ---------------------------------------------------------------------------------------
# Copyright (c) 2015 Polytechnique Montreal <www.neuro.polymtl.ca>
# Author: Julien Cohen-Adad
#
# About the license: see the file LICENSE.TXT
#########################################################################################


import sys
from numpy import concatenate
from msct_parser import Parser
from msct_image import Image


# DEFAULT PARAMETERS
class Param:
    ## The constructor
    def __init__(self):
        self.verbose = 1


# PARSER
# ==========================================================================================
def get_parser():
    # parser initialisation
    parser = Parser(__file__)

    # initialize parameters
    param = Param()
    param_default = Param()

    # Initialize the parser
    parser = Parser(__file__)
    parser.usage.set_description('Concatenate data.')
    parser.add_option(name="-i",
                      type_value=[[','], "file"],
                      description="Multiple files.",
                      mandatory=True,
                      example="data1.nii.gz,data2.nii.gz")
    parser.add_option(name="-o",
                      type_value="file_output",
                      description="Output file",
                      mandatory=True,
                      example=['data_concat.nii.gz'])
    parser.add_option(name="-dim",
                      type_value="multiple_choice",
                      description="""Dimension for concatenation.""",
                      mandatory=True,
                      example=['x', 'y', 'z', 't'])
    return parser


# concatenation
# ==========================================================================================
def concat_data(fname_in, fname_out, dim):
    """
    Concatenate data
    :param fname_in: list of file names.
    :param fname_out:
    :param dim: dimension: 0, 1, 2, 3.
    :return: none
    """

    # Open first file.
    nii = Image(fname_in[0])
    im = nii.data
    # If concatenate in 3rd dimension, add one dimension.
    if dim == 2:
        im = im[:, :, None]
    # If concatenate in 4th dimension, add one dimension.
    if dim == 3:
        im = im[:, :, :, None]
    # Concatenate other files
    for i in range(1, len(fname_in)):
        new_data = Image(fname_in[i]).data
        if dim == 2:
            new_data = new_data[:, :, None]
        if dim == 3:
            new_data = new_data[:, :, :, None]
        im = concatenate((im, new_data), axis=dim)
    # write file
    nii_concat = nii
    nii_concat.data = im
    nii_concat.setFileName(fname_out)
    nii.save()


# MAIN
# ==========================================================================================
def main(args = None):

    dim_list = ['x', 'y', 'z', 't']

    if not args:
        args = sys.argv[1:]

    # Building the command, do sanity checks
    parser = get_parser()
    arguments = parser.parse(sys.argv[1:])
    fname_in = arguments["-i"]
    fname_out = arguments["-o"]
    dim_concat = arguments["-dim"]

    # convert dim into numerical values:
    dim = dim_list.index(dim_concat)

    # convert file
    concat_data(fname_in, fname_out, dim)


# START PROGRAM
# ==========================================================================================
if __name__ == "__main__":
    # initialize parameters
    param = Param()
    # call main function
    main()
