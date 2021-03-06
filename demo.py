#!/usr/bin/env python

# demo.py
# demo script for using abifpy to write fasta files from trace files

import abifpy
import glob

counter = 0

print "Working..."

for trace in glob.glob('*.ab1'):
    abifpy.Trace(trace, trimming=True).write()
    counter += 1

print "Done! Processed {0} trace files.".format(counter)
