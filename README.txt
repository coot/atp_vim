		    Automatic TeX Plugin For Vim version 7.3
			 http://atp-vim.sf.net
		         by Marcin Szamotulski


Supported OS'es: Linux, Mac OS, Windows (it is in development).

Note: support of Windows is not yet fully implemented. The main tools are
not working, yet, come back in a some time (watch the news!).

-------------------------------------------------------------
The directory 'releases' contains stable releases.
The directory 'snapshots' contains unstable releases.

-------------------------------------------------------------
INSTALATION:

To install vimball (vba) file you need to have Vimball Archiver plugin (see 
:h vimball). If you have it, just open the vba file within vim and source it
using the command:
	:source %	(or just :so %)

You can also copy the tar.gz file to your local vim directory (in Linux
$HOME/.vim)a nd extract it.  Then you need to update your helptags. It can be
done with:
	:helptags <path to your doc directory>
See :h helptags (your doc directory is the 'doc' directory inside your local
vim directory.

Now you can read the documentation for ATP with :help atp (this goes to table
of contents, you can also start from beginning with :help
automatic-tex-plugin)

You can find more instructions at
	http://atp-vim.sf.net

-------------------------------------------------------------
HELP:
You can start with :help atp, then
you can get more help subscribing to the mailing list:
    https://lists.sourceforge.net/lists/listinfo/atp-vim-list 
and post your question. I will also announce new releases there.

Some Project NEWS will be post on:
    https://atp-vim.sf.net
------------------------------------------------------------    
Dependencies:

The plugin contains LatexBox developed by D.Munger:
    http://www.vim.org/scripts/script.php?script_id=3109
The code is hosted on Launchpad:
    https://launchpad.net/vim-latex-box

This plugin uses latexmk:
    http://www.phys.psu.edu/~collins/software/latexmk-jcc/
(If you cannot install it, or obtain it there is a command in ATP which does
the same using internal vim language).

GNU wdiff
http://www.gnu.org/software/wdiff/
This is for making word diff of files (see :help atp-:Wdiff).

------------------------------------------------------------
Licence note:

ATP is published under GPL v3+ (see :h atp-copy-rights).
