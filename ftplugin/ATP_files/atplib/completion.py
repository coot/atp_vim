
__all__ = [ cite_pat, ]

import re

def start(pat, string):
    match = re.search(pat, string)
    if match:
        return match.start()
    else:
        return -1

def searchpos(pat, flag):
    """ Search in the buffer for the pat and return its position

    flag: 'b' backward, 'f' forward (default)
    """
    return 0

cite_pat = re.compile(r'\\cite\b(?!.*\\cite\b)')
cite2_pat = re.compile(r'\\(?:no)=cite[^}]*$')
ref_pat = re.compile(r'\\ref\s*{\S*$')
input_pat = re.compile(r'(?:input\s*{[^}]*$|include(?:only)=\s*{[^}]*$|[^\\]\\\\[^\\]$)')
delim_pat = re.compile(r'{|}|,|\^|\$|\(|\)|&|-|\+|=|#|:|;|\.|,|\||\?$')
bracket_pat = re.compile(r'[\[\]\(\){}]')
beginop_pat = re.compile(r'\\begin\s*[[^}]*}\s*\[[^\]]*$')
beginop2_pat = re.compile(r'\\begin\s*[[^}]*}\s*\[[^\]]*\=[^\\,]*$
begend_pat = re.compile(r'(?:\\begin|\\end)\s*$)
label_pat = re.compile(r'(?:\\(?:eq|page|auto|autopage)?ref\*\={[^}]*$|\\hyperref\s*\[[^\]]*$)')
pagestyle_pat = re.compile(r'\\(?:this)=pagestyle{[^}]*$')
pagenumbering_pat = re.compile(r'\\pagenumbering\s*{[^}]*$')
bibitems_pat = re.compile(r'\\(?:no)?[cC]ite((?:al)?[tp]\*\?|text|num|author\*\?|year(?:par)?)?(?:\s*\[[^]]*\]\s*)?{[^}]*$')
tikz1_pat = re.compile(r'(?<!\\def\b.*|\\(?:re)?newcommand\b.*|%.*)\\begin\s*{\s*tikzpicture\s*}')
tikz1_pat = re.compile(r'[^%]*\\end\s*{\s*tikzpicture\s*}')
