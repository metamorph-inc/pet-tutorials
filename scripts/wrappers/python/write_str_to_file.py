from __future__ import print_function
import os
from openmdao.api import Component, FileRef
from pprint import pprint


class WriteStrToFile(Component):

    def __init__(self):
        super(WriteStrToFile, self).__init__()

        # Note: FileRef("{}_input.txt".format(id(self))) is due to an OpenMDAO idiosyncrasy
        #       whenever you have mutiple Components accepting the same FileRef inputs.
        #       In OpenMDAO, FileRef input that share the same name are implicitly linked
        #       even if they aren't explicitly linked...
        #       https://github.com/OpenMDAO/OpenMDAO1/blob/master/openmdao/core/_checks.py#L38
        self.add_param("input_file", val=FileRef("{}_input.txt".format(id(self))), pass_by_obj=True, binary=True)
        self.add_param("input_str", val=u"", pass_by_obj=True)

        self.add_output("output_file", val=FileRef("output.txt"), pass_by_obj=True, binary=True)
        self.add_output("output_str", val=u"", pass_by_obj=True)

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

        # append input str to file text
        f_text += params['input_str'] + "\n"
        print(f_text)
        unknowns['output_str'] = f_text

        # write output file
        with unknowns["output_file"].open("w") as f_out:  # https://openmdao.readthedocs.io/en/1.7.3/usr-guide/tutorials/file-passing.html
            print("Writing to output file: {}".format(unknowns["output_file"]))
            f_out.write(f_text)
