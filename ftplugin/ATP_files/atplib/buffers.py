#!/usr/bin/env python

import vim

__all__ = [ 'read', 'readlines', 'bufnumber' ]


def read(file_path):
    """ Read lines from fname, check if the fname is loaded get tge buffer."""

    for buf in vim.buffers:
	if buf.name == file_path:
            return '\n'.join(buf)
    else:
        with open(file_path, 'r') as fo:
            # we are not decoding: since we have to assume that files are in &encoding
            # vim stores buffers, variables, ... in &encoding.
            return fo.read()

def readlines(file_path):
    """ Read lines from fname, if the fname is loaded get the buffer."""

    for buf in vim.buffers:
	if buf.name == file_path:
            return list(buf)
    else:
        with open(file_path, 'r') as fo:
            # we are not decoding: since we have to assume that files are in &encoding
            # vim stores buffers, variables, ... in &encoding.
            return fo.readlines()

def bufnumber(file, project_dir):
    cdir = os.path.abspath(os.curdir)
    os.chdir(project_dir)
    for buf in vim.buffers:
        # This requires that we are in the directory of the main tex file:
	if buf.name == os.path.abspath(file):
            os.chdir(cdir)
            return buf.number
    for buf in vim.buffers:
	if os.path.basename(buf.name) == file:
            os.chdir(cdir)
            return buf.number
    os.chdir(cdir)
    return 0
