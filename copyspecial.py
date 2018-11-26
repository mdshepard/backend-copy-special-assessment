#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    cmd = 'ls -l ' + dir
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    sfiles = re.findall(r'\w+[_]\.\w+', output)
    spaths = map(lambda x: os.path.abspath(
        os.path.join(dir, x)), sfiles)
    return spaths


def copy_to(paths, dir):
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))


def zip_to(paths, zippath):
    cmd = 'zip -j {} '.format(zippath) + " ".join(paths)
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='origin dir for special files')
    results = parser.parse_args()
    if not results:
        parser.print_usage()
        sys.exit(1)
    todir = results.todir
    from_dir = results.from_dir
    tozip = results.tozip
    spaths = get_special_paths(from_dir)
    if todir:
        copy_to(spaths, todir)
    elif tozip:
        zip_to(spaths, tozip)
    else:
        print "\n".join(spaths)


if __name__ == "__main__":
    main()
