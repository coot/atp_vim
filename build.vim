let g:vimball_home	= "."
edit Makefile
g!/^SOURCE/d
%s/^SOURCE\s*+\?=\s*//
execute '%MkVimball!' . g:plugin_name
