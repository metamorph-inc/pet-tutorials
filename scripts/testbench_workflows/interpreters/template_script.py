from __future__ import unicode_literals
import _winreg as winreg
import sys
from os.path import join, isfile
from os import makedirs
import pprint


with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'Software\META') as software_meta:
    meta_path, _ = winreg.QueryValueEx(software_meta, 'META_PATH')
sys.path.append(join(meta_path, 'bin'))

import udm


# This is the entry point
def invoke(focusObject, rootObject, componentParameters, **kwargs):
    log('Running elaborator')
    elaborate(focusObject)
    log(pprint.pformat(componentParameters))

    path_udm_xml = join(meta_path, r'generated\CyPhyML\models\CyPhyML_udm.xml')
    if not isfile(path_udm_xml):
        path_udm_xml = join(meta_path, r'meta\CyPhyML_udm.xml')

	log("Interpreters allow you to access the model directly. Too bad this one doesn't really do anything...")
	
    # YOUR CODE HERE...
	log("YOUR CODE HERE...")

    componentParameters['runCommand'] = 'cmd.exe /c dir'


# CyPhyPython boilerplate stuff
def log(s):
    print s  # prints to /results/RESULTS_FOLDER/log/CyPhyPython.txt


try:
    import CyPhyPython  # will fail if not running under CyPhyPython
    import cgi


    def log(s):
        CyPhyPython.log(cgi.escape(s))
except ImportError:
    pass


def log_formatted(s):
    print s


try:
    import CyPhyPython  # will fail if not running under CyPhyPython
    import cgi


    def log(s):
        CyPhyPython.log(s)
except ImportError:
    pass

def elaborate(focusObject):
    import win32com.client.dynamic
    elaborator = win32com.client.dynamic.Dispatch('MGA.Interpreter.CyPhyElaborateCS')
    succeeded = elaborator.RunInTransaction(focusObject.convert_udm2gme().Project, focusObject.convert_udm2gme(),
                                            win32com.client.dynamic.Dispatch('Mga.MgaFCOs'), 128)
    if not succeeded:
        raise RuntimeError('Elaborator failed')