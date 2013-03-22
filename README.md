[Automatic TeX Plugin](http://atp-vim.sf.net) For [Vim](http://vim.org) version 7.3
========================================

Supported OS'es: *Linux*, *Mac OS*, *Windows* (some features are not working).

Visit http://atp-vim.sf.net to get more info: features, videos presenting some
functionalities, online help. Just to list the main features:

 * background processing with a progress bar,
 * forward/inverse search for okular, evince, xpdf, open (on MacOs),
 * compilation of projects, or just parts of projects (using the subfiles
 LaTeX package),
 * excellent completion, which also closes environments and brackets, and
 inputting labels by their numbers (as seen in the output) and much more ...
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
D.Munger. LatexBox is developed on [GitHub](https://github.com/LaTeX-Box-Team/LaTeX-Box).
It uses [latexmk](http://www.phys.psu.edu/~collins/software/latexmk-jcc/)
(If you cannot install it, or obtain it there is a command in _ATP_ which does
the same, but also prints a progress information on the *Vim* status line.).

*GNU* [wdiff](http://www.gnu.org/software/wdiff/) for making word
diffs (see ":help atp-:Wdiff").

Windows:
--------

The progress bar and callback features are turned off on Windows.  The reason
is how vim-server works on windows: whenever one calls back it shows a window
with message ERROR 0, which is quite annoying especially since compilation
script calls back vim several times.  ATP is not thoroughly tested on Windows
so something might not work.  Drop me an email or write to the mailing list,
and note that its about ATP on Windows.

Licence note:
-------------

ATP is published under *GPL v3+*.

Copyright: Marcin Szamotulski, © 2011, 2012, 2013
