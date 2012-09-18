#!/usr/bin/env python

import vim

__all__ = [ 'read', 'readlines', 'bufnumber' ]

def bufnumber(fpath):
    """ Return bufer number of fpath,

    fpath should be a full path of a file.
    """
    for buf in vim.buffers:
	if buf.name == fpath:
            return buf.number
    else:
        return 0

def read(file_path):
    """ Read lines from fname, check if the fname is loaded get tge buffer."""

    bufnr = bufname(file_path)
    if bufnr:
        return "\n".join(vim.buffers[bufnr-1])
    else:
        with open(file_path, 'r') as fo:
            # we are not decoding: since we have to assume that files are in &encoding
            # vim stores buffers, variables, ... in &encoding.
            return fo.read()

def readlines(file_path):
    """ Read lines from fname, if the fname is loaded get the buffer."""

    bufnr = bufnumber(file_path)
    if bufnr:
        return vim.buffers[bufnr-1]
    else:
        with open(file_path, 'r') as fo:
            # we are not decoding: since we have to assume that files are in &encoding
            # vim stores buffers, variables, ... in &encoding.
            return fo.readlines()
