from __future__ import print_function
import os
from openmdao.api import Component, FileRef
from pprint import pprint


class WriteStrToFile(Component):

    def __init__(self):
        super(WriteStrToFile, self).__init__()

        self.add_param("input_file", val=FileRef("input.txt"), pass_by_obj=True, binary=True)
        self.add_param("input_str", val=u"", pass_by_obj=True, binary=True)

        self.add_output("output_file", val=FileRef("output.txt"), pass_by_obj=True, binary=True)

    def solve_nonlinear(self, params, unknowns, resids):
        f_text = ""

        # FIXME: Handle 2 cases:
        # FIXME:   No Output connected to input file
        # FIXME:   Output connected - but no file provided

        # read input file if provided
        try:
            with params['input_file'].open("r") as f_in:
                f_text = f_in.read()
                print("input file: {}".format(params['input_file']))
                print(f_text)
        except IOError:
            print("No input file: {}".format(params['input_file']))
        else:
            f_in.close()

        # append input str to file text
        f_text += params['input_str'] + "\n"

        # write output file
        f_name = "output.txt"
        with open("output.txt", 'w') as f_out:
            print("Writing to output file ({}):".format(f_name))
            print(f_text)
            f_out.write(f_text)

        unknowns['output_file'] = FileRef(f_name, os.getcwd())
