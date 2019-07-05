#!/usr/bin/env python
#########################################################################################
#
# Concatenate transformations. This function is a wrapper for isct_ComposeMultiTransform
#
# ---------------------------------------------------------------------------------------
# Copyright (c) 2014 Polytechnique Montreal <www.neuro.polymtl.ca>
# Authors: Julien Cohen-Adad
# Modified: 2014-07-20
#
# About the license: see the file LICENSE.TXT
#########################################################################################

# TODO: also enable to concatenate reversed transfo

from __future__ import absolute_import, division

import sys, os, functools, argparse

import sct_utils as sct
from spinalcordtoolbox.image import Image
from spinalcordtoolbox.utils import Metavar

class Param:
    # The constructor
    def __init__(self):
        self.fname_warp_final = 'warp_final.nii.gz'


def main(args=None):
    """
    Main function
    :param args:
    :return:
    """
    # get parser args
    if args is None:
        args = None if sys.argv[1:] else ['--help']
    parser = get_parser()
    arguments = parser.parse_args(args=args)

    # Initialization
    fname_warp_final = ''  # concatenated transformations
    fname_dest = arguments.d
    fname_warp_list = (arguments.w).split(",")

    if arguments.o is not None:
        fname_warp_final = arguments.o
    verbose = arguments.v
    sct.init_sct(log_level=verbose, update=True)  # Update log level

    # Parse list of warping fields
    sct.printv('\nParse list of transformations...', verbose)
    use_inverse = []
    fname_warp_list_invert = []
    for i in range(len(fname_warp_list)):
        # Check if inverse matrix is specified with '-' at the beginning of file name
        if fname_warp_list[i].find('-') == 0:
            use_inverse.append('-i')
            fname_warp_list[i] = fname_warp_list[i][1:]  # remove '-'
            fname_warp_list_invert += [[use_inverse[i], fname_warp_list[i]]]
        else:
            use_inverse.append('')
            fname_warp_list_invert += [[fname_warp_list[i]]]
        sct.printv('  Transfo #' + str(i) + ': ' + use_inverse[i] + fname_warp_list[i], verbose)

    # Check file existence
    sct.printv('\nCheck file existence...', verbose)
    sct.check_file_exist(fname_dest, verbose)
    for i in range(len(fname_warp_list)):
        sct.check_file_exist(fname_warp_list[i], verbose)

    # Get output folder and file name
    if fname_warp_final == '':
        path_out, file_out, ext_out = sct.extract_fname(param.fname_warp_final)
    else:
        path_out, file_out, ext_out = sct.extract_fname(fname_warp_final)

    # Check dimension of destination data (cf. issue #1419, #1429)
    im_dest = Image(fname_dest)
    if im_dest.dim[2] == 1:
        dimensionality = '2'
    else:
        dimensionality = '3'

    # Concatenate warping fields
    sct.printv('\nConcatenate warping fields...', verbose)
    # N.B. Here we take the inverse of the warp list
    fname_warp_list_invert.reverse()
    fname_warp_list_invert = functools.reduce(lambda x,y: x+y, fname_warp_list_invert)

    cmd = ['isct_ComposeMultiTransform', dimensionality, 'warp_final' + ext_out, '-R', fname_dest] + fname_warp_list_invert
    status, output = sct.run(cmd, verbose=verbose, is_sct_binary=True)

    # check if output was generated
    if not os.path.isfile('warp_final' + ext_out):
        sct.printv('ERROR: Warping field was not generated.\n' + output, 1, 'error')

    # Generate output files
    sct.printv('\nGenerate output files...', verbose)
    sct.generate_output_file('warp_final' + ext_out, os.path.join(path_out, file_out + ext_out))


# ==========================================================================================
def get_parser():
    # Initialize the parser

    parser = argparse.ArgumentParser(
        description='Concatenate transformations. This function is a wrapper for isct_ComposeMultiTransform (ANTs). N.B. Order of input warping fields is important. For example, if you want to concatenate: A->B and B->C to yield A->C, then you have to input warping fields like that: A->B,B->C.',
        add_help=None,
        prog=os.path.basename(__file__).strip(".py"))
    mandatoryArguments = parser.add_argument_group("\nMANDATORY ARGUMENTS")
    mandatoryArguments.add_argument(
        "-d",
        help='Destination image. (e.g. "mt.nii.gz")',
        metavar=Metavar.file,
        required=False)
    mandatoryArguments.add_argument(
        "-w",
        help='List of affine matrix or warping fields separated with "," N.B. if you want to use the inverse matrix, add "-" before matrix file name. N.B. You should NOT use "-" with warping fields (only with matrices). If you want to use an inverse warping field, then input it directly (e.g. "warp_template2anat.nii.gz" instead of "warp_anat2template.nii.gz") ',
        metavar=Metavar.list,
        required = False)
    optional = parser.add_argument_group("\nOPTIONAL ARGUMENTS")
    optional.add_argument(
        "-h",
        "--help",
        action="help",
        help="show this help message and exit")
    optional.add_argument(
        "-o",
        help='Name of output warping field (e.g. "warp_template2mt.nii.gz")',
        metavar=Metavar.str,
        required = False)
    optional.add_argument(
        "-v",
        type=int,
        help="Verbose: 0 = nothing, 1 = classic, 2 = expended",
        required=False,
        choices=(0, 1, 2),
        default = 1)

    return parser


#=======================================================================================================================
# Start program
#=======================================================================================================================
if __name__ == "__main__":
    sct.init_sct()
    param = Param()
    # call main function
    main()
