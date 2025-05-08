#!/usr/bin/env python3

"""
SCons build file for updating .html when corresponding .txt files change.
"""

import os
from pprint import pprint

#import sys
#from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')

# pythonenv = Environment()
# pythondb_site = os.path.join(os.path.expanduser('~'),'.scons','site_scons','site_tools','rest')
# pythonenv.Install(db_site, '__init__.py')
# pythonenv.Alias('install', db_site)

env = Environment(tools=['rest'])

to_prune = {}

# Find all .html files with an associated .txt file, and strip off the .html
# extensions:
build_files = []
for root, dirs, files in os.walk('.'):
    #print(root)
    for d in dirs:
        path = os.path.join(root, d)
        if (d == 'en') or (path in to_prune):
            dirs.remove(d)
            print('pruned: {}'.format(path))
    for f in files:
        if f.endswith('.html'):
            if os.path.exists(os.path.join(root, f.replace('.html', '.txt'))):
                build_files.append(os.path.splitext(os.path.join(root, f))[0])
            #else:
            #    print(os.path.join(root,f))

#pprint(build_files)

# You can call Default many times to add to the default target list.
# Need to specify matching lists of target & source files, to allow file names
# with embedded periods ('.'); otherwise, these files don't work:
t = env.Rst2Html(
    [f + '.html' for f in build_files], [f + '.txt' for f in build_files])
Default(t)
