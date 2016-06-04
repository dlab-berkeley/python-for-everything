#!/bin/env python

# In this challenge, we are going to fix up a program that attempts to use
# regular expressions to grab all of the URLs out of any number of files.
# Spend some time thinking about how URLs are formatted -- what do they
# all have in common? What always stays the same? What is optional? What
# characters are not allowed? What is allowed to repeat?

def read_file(fp):
    """Read in a file, given a filepath, and return a string"""
    with open(fp, 'r') as f:
        document = f.read()

def get_url_list(document):
    """Return a list of URLs from a string"""
    if not isinstance(document, str):
        raise ValueError("document is not a string")
    p = re.compile(r'(?:http://)([a-z].[com]{2,6}[a-z/])', flags=re.I)
    return p.findall(document)

def process_files(*args):
    """
    Get URLs from an arbitrary number of filepaths, and return a dictionary whose keys are filepaths and whose values are lists of URLs
    """
    url_dictionary = {}
    for fp in args:
        document = read_file(fp)
        url_dictionary = get_url_list(document)
    return url_dictionary

## The stuff below here is okay -- no need to fix it!
## If you want to try out this program yourself, you can run it from the
## command line with `python A_re.py ../../README.md` and see this:
## README.md :
##   - github.com/dlab-berkeley/python-for-everything
##   - python.berkeley.edu/resources/
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filepaths', nargs='+')
    args = parser.parse_args()

    results = process_files(*args.filepaths)
    for key, value in results.items():
        print(key, ':')
        for url in value:
            print('  -', url)
