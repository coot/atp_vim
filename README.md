[Automatic TeX Plugin](http://atp-vim.sf.net) For [Vim](http://vim.org) version 7.3
========================================

Supported OS'es: *Linux*, *Mac OS*, *Windows* (not quite!, your welcome to
help - ask me how to and I will be happy to provide help).

Visit http://atp-vim.sf.net to get more info: features, vidoes presenting some
functionalities, online help. Just to list the main features:

 * background processing with a progress bar,
 * forward/inverse search for okular, evince, xpdf, open (on MacOs),
 * compilation of projects, or just parts of projects (using the subfiles
 LaTeX package),
 * excelent completion, which also closes environments and brackets, and
 inputing labels by their numbers (as seen in the output) and much more ...
 * table of contents,
 * do you want to see [more](http://atp-vim.sf.net) ... / even that is not complete ... /


_ATP_ is written in *Python* and *VimL*.

Help:
-----

You can start with ":help atp". You also subscribe to the [mailing
list](https://lists.sourceforge.net/lists/listinfo/atp-vim-list) and post your
question there.

Dependencies:
-------------

The plugin contains:
[LatexBox](http://www.vim.org/scripts/script.php?script_id=3109) developed by
D.Munger. LatexBox is developed [GitHub](https://github.com/LaTeX-Box-Team/LaTeX-Box).
It uses [latexmk](http://www.phys.psu.edu/~collins/software/latexmk-jcc/)
(If you cannot install it, or obtain it there is a command in ATP which does
the same using internal vim language).

*GNU* [wdiff](http://www.gnu.org/software/wdiff/) for making word
diffs (see ":help atp-:Wdiff").


Licence note:
-------------

ATP is published under *GPL v3+*.

Copyright: Marcin Szamotulski, © 2011, 2012
