from glob import glob

import pycallgraph

examples = glob('*.py')
examples.remove('all.py')
for example in examples:
    pycallgraph.reset_settings()
    execfile(example)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
