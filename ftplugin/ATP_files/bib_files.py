#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Christian Becke <christianbecke[@]gmail[.]com>
# This file is a part of Automatic TeX Plugin for Vim.

import os
import os.path
import fnmatch
import shutil
import errno

def add_bib_files (src, dest, tempdir):
    src = os.path.realpath (src)
    dest = os.path.realpath (dest)

    for root, dirnames, filenames in os.walk (src):
        matches = []
        for filename in fnmatch.filter (filenames, "*.bib"):
            matches.append (filename)

        if matches:
            # symlink, or, if symlinking fails, copy bib files
            relroot = root.replace (src, "").lstrip ("/")
            d = os.path.join (dest, relroot)
            try:
                os.makedirs (d)
            except OSError, e:
                # no problem if d allready exists...
                if e.errno != errno.EEXIST:
                    raise
            for match in matches:
                symlinked = False
                try:
                    os.symlink (os.path.join (root, match), os.path.join (d, match))
                    symlinked = True
                except OSError, e:
                    # no problem if symlink allready exists...
                    if e.errno == errno.EEXIST:
                        symlinked = True

                if not symlinked:
                    shutil.copy (os.path.join (root, match), os.path.join (d, match))

        # do not recurse into dest or tmpdir
        skipdirs = []
        for d in dirnames:
            # compare path strings first, os.path.samefile calls stat() and
            # might be slow
            if dest.endswith (d) and os.path.samefile (dest, os.path.join (root, d)):
                skipdirs.append (d)
            elif tempdir.endswith (d) and os.path.samefile (tempdir, os.path.join (root, d)):
                skipdirs.append (d)
        for d in skipdirs:
            dirnames.remove (d)

