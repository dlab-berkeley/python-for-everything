#!/bin/env python

# In this challenge, you are going to use your newfound knowledge of
# control flow and exception handling to fix the following program.
# Its intention, which you'll see as you read through the code blocks
# below, is to back up the files in a directory.

from glob import glob
import os
import time

def backup_files():
    os.mkdir('backup') # make a directory
    filename = time.asctime().replace(' ', '_').replace(':', '-') # make a string out of the current time with weird characters replaced
    with open(os.path.join('backup', filename), 'a') as f: # open file with filename in the backup folder for appending text
        for filepath in glob('*'): # matches any path in current directory
            with open(filepath, 'r') as g:
                f.write('\n\n' + filepath + '\n' + g.read()) # write to f the output of g.read()

if __name__ == '__main__':
    backup_files()
