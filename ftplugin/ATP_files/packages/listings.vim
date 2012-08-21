" This file is a part of ATP 
" Author: Marcin Szamotulski

let g:atp_listings_commands = [ '\lstset{', '\lstinline', '\lstinputlisting', '\lstaspectfiles', '\lstlistingname', '\lstlistlistingname', '\thelstisting', '\lstname', '\lstnewenvironment{', '\lstMakeShortInline', '\lstDeleteShortInline', '\lstdefinelanguage', '\lstalias' ]

let s:keys = [ 'style=', 'language=', 'alsolanguage=', 'defaultdialect=', 'printpod=', 'usekeywordsintag=', 'tagstyle=', 'markfirstintag=', 'makemacrouse=', 'basicstyle=', 'keywordstyle=', 'identifierstyle=', 'commentstyle=', 'stringstyle=', 'showspaces=', 'showstringspaces=', 'numbers=', 'numberstyle=', 'stepnumber=', 'numbersep=', 'showtabs=', 'tab=', 'formfeed=', 'extendedchars=', 'firstnumber=', 'frame=', 'aboveskip=', 'belowskip=', 'frameround=', 'backgroundcolor=', 'emph=', 'emphstyle=', 'index', 'columns=', 'numberbychapter=', 'captionpos=', 'abovecaptionskip=', 'belowcaptionskip=', 'linewidth=', 'xleftmargin=', 'xrightmargin', 'resetmargins=', 'breaklines', 'breakatwhitespaces',  'prebreak=', 'postbreak=', 'breakindent=', 'breakautoindent=', 'framesep=', 'rulesep=', 'framerule=', 'framexleftmargin=', 'framexrightmargin=', 'framextopmargin=', 'framexbottommaring=', 'rulecolor=', 'fillcolor=', 'rulesepcolor=', 'index=', 'indexstyle=', 'flexiblecolums', 'keepspaces=', 'basewidth=', 'fontadjust', 'texcl', 'mathescape=', 'escapechar=', 'escapeinside=', 'escapebeing=', 'escapeend=', 'fancyvrb=', 'fvcmdparams=', 'morevfcmdparams=' ]
let s:languages = [ 'ABAP', 'ACSL', 'Algol', 'Ada', 'Ant', 'Assembler', 'Awk', 'bash', 'Basic', 'C', '[Handel]C', '[Objective]C', '[Sharp]C', '[Visual]C++', "[ISO]C++", "C++", '[GNU]C++', 'Caml', 'Cobol', 'Comal', 'command.com', 'Comsol', 'csh', 'Delphi', 'Eiffel', 'Elan', 'erlang', 'Euphoria', 'Fortran', 'GCL', 'Gnuplot', 'Haskell', 'HTML', 'IDL', 'ifnorm', 'ksh', 'Lingo', 'Lisp', 'Logo', 'make', 'Mathematica', 'Matlab', 'Mercury', 'MetaPost', 'Miranda', 'Mizar', 'ML', 'Modula-2', 'MuPAD', 'NASTRAN', 'Oberon-2', 'OCL', 'Octave', 'Oz', 'Pascal', 'Perl', 'PHP', 'PL/I', 'Plasm', 'PostScript', 'POV', 'Prolog', 'Promela', 'PSTricks', 'Python', 'R', 'Reduce', 'Rexx', 'RSL', 'Ruby', 'S', 'SAS', 'Scilab', 'sh', 'SHELXL', 'Simula', 'SPARQL', 'SQL', 'tel', 'TeX', '[LaTeX]TeX', '[primitive]TeX', '[AlLaTeX]TeX', '[common]TeX', 'VBScript', 'Verilog', 'VHDL', 'VRML', 'XML', 'XSLT']
let g:atp_listings_command_values = {
	    \ '\\lstset{' : s:keys,
	    \ '\\lstloadlanguages{' : s:languages
	    \ }
function! ATP_listings_environments()
    let env_list = ['lstlisting']
" TURN OFF -> leads to problems when opening a second tex file. Probably
" because of call to lvimgreee inside atplib#various#Preamble() function.
"     let preamble = atplib#various#Preamble(1)
"     for line in preamble
" 	for sub_line in split(line, '\ze\\lstnewenvironment')
" 	    let env = matchstr(sub_line, '\\lstnewenvironment\s*{\s*\zs[^}]*\ze\s*}')
" 	    if !empty(env)
" 		call add(env_list, env)
" 	    endif
" 	endfor
"     endfor
    return env_list
endfunction
let g:atp_listings_environments = ATP_listings_environments() " Scan the preamble for \lstnewenvironment command.
let g:atp_listings_environment_options = { join(g:atp_listings_environments, '\|') : s:keys+['caption=', 'title=', 'label=', 'nolol=' ] }
let s:options_values = {
		\'\%(also\)\?language' : s:languages, 
		\ 'nolol\|resetmargins\|break\%(lines\|atwhitespace\|autoindent\)\|show\%(string\)\?spaces\|flexiblespacs\|keepspaces\|fontadjust\|mathescape\|fancyvrb' : [ 'true', 'false' ],
		\ 'columns' : { 'matches' : [ 'fixed', 'flexible', 'spaceflexible', 'fullflexible' ], 'ignore_pattern' : '\%(\[[clr]\]\)\='},
		\ 'frame' : [ 'none', 'leftline', 'topline', 'bottomline', 'lines', 'single', 'shadowbox' ],
		\ 'numbers' : [ 'none', 'left', 'right' ],
		\ 'captionpos' : [ 'b', 't' ],
		\ }
" The dictionary of values of command values:
let g:atp_listings_command_values_dict = { '\\lstset' : s:options_values }
let g:atp_listings_environment_options_values = { join(g:atp_listings_environments, '\|') : s:options_values }
