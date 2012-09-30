
__all__ = [ 'start', 'searchpos', 'index', 'cite_pat', 'cite2_pat', 'ref_pat',
            'input_pat', 'delim_pat', 'bracket_pat', 'begend_pat',
            'beginop_pat', 'beginop2_pat', 'label_pat', 'pagestyle_pat',
            'pagenumbering_pat', 'bibitems_pat', 'tikz1_pat', 'tikz3_pat' ]

import vim
import re

def start(pat, string):
    match = re.search(pat, string)
    if match:
        return match.start()
    else:
        return -1

def searchpos(pat, flag=''):
    """ Search in the buffer for the pat and return its position

    flag: 'b' backward, 'f' forward (default)."""
    buf = vim.current.buffer
    (linenr, col) = vim.current.window.cursor
    if 'b' in flag:
        line = buf[linenr-1]
        for i in range(col)[::-1]:
            l = line[i:]
            match = re.match(pat, l)
            if match:
                return (linenr, i+1)
        while linenr >= 0:
            linenr -= 1
            line = buf[linenr-1]
            for i in range(len(line))[::-1]:
                l = line[i:]
                if re.match(pat, l):
                    return (linenr, i+1)
        else:
            return (0,0)
    else:
        line = buf[linenr-1][col:]
        print line
        match = re.search(pat, line)
        if match:
            return (linenr, match.start()+col+1)
        while linenr <= len(buf):
            linenr += 1
            line = buf[linenr-1]
            match = re.search(pat, line)
            if match:
                return (linenr, match.start()+1)
        else:
            return (0,0)

    return 0

def index(char, string):
    if char in string:
        return string.index(char)
    else:
        return -1

cite_pat = re.compile(r'\\cite\b(?!.*\\cite\b)')
cite2_pat = re.compile(r'\\(?:no)?cite[^}]*$')
ref_pat = re.compile(r'\\ref\s*{\S*$')
input_pat = re.compile(r'(?:input\s*{[^}]*$|include(?:only)=\s*{[^}]*$|[^\\]\\\\[^\\]$)')
delim_pat = re.compile(r'{|}|,|\^|\$|\(|\)|&|-|\+|=|#|:|;|\.|,|\||\?$')
bracket_pat = re.compile(r'[\[\]\(\){}]')
beginop_pat = re.compile(r'\\begin\s*{[^}]*}\s*\[[^\]]*$')
beginop2_pat = re.compile(r'\\begin\s*{[^}]*}\s*\[[^\]]*=[^\\,]*$')
begend_pat = re.compile(r'(?:\\begin|\\end)\s*$')
label_pat = re.compile(r'(?:\\(?:eq|page|auto|autopage)?ref\*?{[^}]*$|\\hyperref\s*\[[^\]]*$)')
pagestyle_pat = re.compile(r'\\(?:this)?pagestyle\s*{[^}]*$')
pagenumbering_pat = re.compile(r'\\pagenumbering\s*{[^}]*$')
bibitems_pat = re.compile(r'\\(?:no)?[cC]ite((?:al)?[tp]\*\?|text|num|author\*\?|year(?:par)?)?(?:\s*\[[^]]*\]\s*)?{[^}]*$')
# tikz1_pat = re.compile(r'(?<!\\def\b.*|\\(?:re)?newcommand\b.*|%.*)\\begin\s*{\s*tikzpicture\s*}')
# XXX: look behind requires a fixed length pattern
tikz1_pat = re.compile(r'\\begin\s*{\s*tikzpicture\s*}')
# tikz2_pat = re.compile(r'(?:<\\def\b.*|\\(?:re)?newcommand\b.*|%.*)\\begin\s*{\s*tikzpicture\s*}')
tikz3_pat = re.compile(r'[^%]*\\end\s*{\s*tikzpicture\s*}')
tikzdelim_pat = re.compile(r'(?:\s|\[|{|}|,|\.|=|:)$')
