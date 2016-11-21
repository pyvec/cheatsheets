#! /usr/bin/env python3

import glob
import re
import subprocess
import shlex

lines = []
for filename in glob.glob('*/*.svg'):
    output = re.sub(r'\.svg$', '.pdf', filename)
    lines.append([filename, '-A', output])

proc = subprocess.Popen(['inkscape', '--shell'], stdin=subprocess.PIPE)
stdin_text = '\n'.join(' '.join(shlex.quote(w) for w in s) for s in lines) + '\n'
print(stdin_text)
proc.communicate(stdin_text.encode('utf-8'))
print()
