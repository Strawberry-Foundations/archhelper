import yaml
import sys

def load_module(file):
    with open(file) as m:
        module = yaml.load(m, Loader=yaml.SafeLoader)
        return module

