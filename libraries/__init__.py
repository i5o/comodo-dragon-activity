import sys
import os

def setup_path():
    modules = ['sugargame2', 'spyral', 'parsley']
    for module in modules:
        sys.path.insert(0, os.path.abspath('libraries/%s/' % module))
