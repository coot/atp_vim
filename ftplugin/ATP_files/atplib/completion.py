
__all__ = [ cite_pat, ]

import re

cite_pat = re.compile(r'\\cite\b(?!.*\\cite\b)')
input_pat = re.compile(r'(?:input\s*{[^}]*$|include(?only)=\s*{[^}]*$|[^\\]\\\\[^\\]$')
