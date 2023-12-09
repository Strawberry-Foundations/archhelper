#!/usr/bin/env python3

import sys
import os

import src.ParseModule as pm

try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

module = None

if (arg == ""):
    print("Please provide a module to load.")
    sys.exit(1)

if (os.path.exists(arg)):
    print("Detected file, trying to load module...")
    module = pm.load_module(arg)
    print(module)
else:
    print("ERROR: File does not exist.")
