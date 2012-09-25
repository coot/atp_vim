
__all__ = [ cite_pat, ]

import re

cite_pat = re.compile(r'\\cite\b(?!.*\\cite\b)')
cite2_pat = re.compile(r'\\(?:no)=cite[^}]*$')
ref_pat = re.compile(r'\\ref\s*{\S*$')
input_pat = re.compile(r'(?:input\s*{[^}]*$|include(?:only)=\s*{[^}]*$|[^\\]\\\\[^\\]$)')
delim_pat = re.compile(r'{|}|,|\^|\$|\(|\)|&|-|\+|\=|#|:|;|\.|,|\||\?$')
bracket_pat = re.compile(r'[\[\]\(\){}]')
