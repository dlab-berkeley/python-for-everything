#!/bin/env python

# In this challenge, you are going to use your newfound knowledge of
# exception handling to refactor the following script so that it works
# properly

from glob import glob
import os
import time

def backup_files():
    os.mkdir('backup')
    filename = time.asctime().replace(' ', '_').replace(':', '-')
    with open(os.path.join('backup', filename), 'a') as f:
        for filepath in glob('*'):
            with open(filepath, 'r') as g:
                f.write('\n\n' + filepath + '\n' + g.read())

if __name__ == '__main__':
    backup_files()
