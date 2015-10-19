#! /usr/bin/env python3

import glob
import re
import subprocess

for filename in glob.glob('*/*.svg'):
    print(filename)
    output = re.sub(r'\.svg$', '.pdf', filename)
    subprocess.check_call(['inkscape', filename, '-A', output])
