" This file is a part of ATP 
" Author: Marcin Szamotulski

let g:atp_listings_commands = [ '\lstset{', '\lstinline', '\lstinputlisting', '\lstaspectfiles', '\lstlistingname', '\lstlistlistingname', '\thelstisting', '\lstname', '\lstnewenvironment{', '\lstMakeShortInline', '\lstDeleteShortInline', '\lstdefinelanguage', '\lstalias' ]

let s:keys = [ 'basicstyle=', 'keywordstyle=', 'identifierstyle=', 'commentstyle=', 'stringstyle=', 'showstringspaces=', 'numbers=', 'numberstyle=', 'stepnumber=', 'numbersep=', 'showtabs=', 'tab=', 'formfeed=', 'extendedchars=', 'firstnumber=', 'frame=', 'aboveskip=', 'belowskip=', 'frameround=', 'backgroundcolor=', 'emph=', 'emphstyle=', 'index', 'columns=', 'numberbychapter=', 'captionpos=', 'abovecaptionskip=', 'belowcaptionskip=', 'linewidth=', 'xleftmargin=', 'xrightmargin', 'resetmargins=', 'breaklines', 'breakatwhitespaces',  'prebreak=', 'postbreak=', 'breakindent=', 'breakautoindent=', 'framesep=', 'rulesep=', 'framerule=', 'framexleftmargin=', 'framexrightmargin=', 'framextopmargin=', 'framexbottommaring=', 'rulecolor=', 'fillcolor=', 'rulesepcolor=', 'index=', 'indexstyle=', 'flexiblecolums', 'keepspaces=', 'basewidth=', 'fontadjust', 'texcl', 'mathescape=', 'escapechar=', 'escapeinside=', 'escapebeing=', 'escapeend=', 'fancyvrb=', 'fvcmdparams=', 'morevfcmdparams=' ]
let s:languages = [ 'ABAP', 'ACSL', 'Algol', 'Ada', 'Ant', 'Assembler', 'Awk', 'bash', 'Basic', 'C', '[Handel]C', '[Objective]C', '[Sharp]C', '[Visual]C++', "[ISO]C++", "C++", '[GNU]C++', 'Caml', 'Cobol', 'Comal', 'command.com', 'Comsol', 'csh', 'Delphi', 'Eiffel', 'Elan', 'erlang', 'Euphoria', 'Fortran', 'GCL', 'Gnuplot', 'Haskell', 'HTML', 'IDL', 'ifnorm', 'ksh', 'Lingo', 'Lisp', 'Logo', 'make', 'Mathematica', 'Matlab', 'Mercury', 'MetaPost', 'Miranda', 'Mizar', 'ML', 'Modula-2', 'MuPAD', 'NASTRAN', 'Oberon-2', 'OCL', 'Octave', 'Oz', 'Pascal', 'Perl', 'PHP', 'PL/I', 'Plasm', 'PostScript', 'POV', 'Prolog', 'Promela', 'PSTricks', 'Python', 'R', 'Reduce', 'Rexx', 'RSL', 'Ruby', 'S', 'SAS', 'Scilab', 'sh', 'SHELXL', 'Simula', 'SPARQL', 'SQL', 'tel', 'TeX', '[LaTeX]TeX', '[primitive]TeX', '[AlLaTeX]TeX', '[common]TeX', 'VBScript', 'Verilog', 'VHDL', 'VRML', 'XML', 'XSLT']
let g:atp_listings_command_values = {
	    \ '\\lstset{' : s:keys,
	    \ '\\lstloadlanguages{' : s:languages
	    \ }

let g:atp_listigns_environments = [ 'lstlisting' ]
let g:atp_listings_environment_options = { 'lstlisting' : s:keys+['caption=', 'title=', 'label=', 'nolol=' ] }
