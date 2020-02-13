import os
import json


def load_json_file(filename):
    print("Opening {} ...".format(filename))
    json_dict = None
    try:
        with open(filename) as f_in:
            json_dict = json.load(f_in)
    except IOError:
        print("No {} file found.".format(filename))
        pass
    return json_dict


def main():
    tb_manifest = load_json_file("testbench_manifest.json")

    params = {}
    file_inputs = {}
    metrics = {}
    file_outputs = {}

    # Read from testbench manifest
    for tb_param in tb_manifest['Parameters']:
        params[tb_param['Name']] = tb_param['Value']
    for tb_metric in tb_manifest['Metrics']:
        metrics[tb_metric['Name']] = tb_metric['Value']
    for tb_fileinput in tb_manifest['FileInputs']:
        file_inputs[tb_fileinput['Name']] = tb_fileinput['FileName']
    for tb_fileoutput in tb_manifest['FileOutputs']:
        file_outputs[tb_fileoutput['Name']] = tb_fileoutput['FileName']

    f_text = ""

    # read input file if provided
    try:
        with open(file_inputs['input_file'], "r") as f_in:
            f_text = f_in.read()
            print("input file: {}".format(file_inputs['input_file']))
            print(f_text)
    except IOError:
        print("No input file: {}".format(file_inputs['input_file']))

    # append input str to file text
    f_text += params['input_str'] + "\n"
    print(f_text)
    # metrics['output_str'] = f_text  # FIXME: Test Bench current do not support non-float outputs

    # write output file
    print(file_outputs['output_file'])
    with open(file_outputs['output_file'], "w") as f_out:  # https://openmdao.readthedocs.io/en/1.7.3/usr-guide/tutorials/file-passing.html
        print("Writing to output file: {}".format(file_outputs["output_file"]))
        f_out.write(f_text)


if __name__ == '__main__':
    main()
