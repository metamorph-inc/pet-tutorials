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


if __name__ == '__main__':
    main()