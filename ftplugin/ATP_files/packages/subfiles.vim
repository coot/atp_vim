" This file is a part of ATP.
" Written by Marcin Szamotulski <atp-list@lists.sourceforge.net>
let  g:atp_subfiles_options = { }
function! g:atp_subfiles_options.GetOptions(path) dict
    let dir = expand("%:p:h")."/".fnamemodify(a:path, ":h")
    let file = fnamemodify(a:path, ":t")

    let list = map(split(globpath(dir, file."*")), "fnamemodify(v:val, ':s?^'.dir.'/\\=??:r')")
    let f_list = []
    for i in list
	if index(f_list, i) == -1
	    call add(f_list, i)
	endif
    endfor
    return f_list
endfunction
