#!/usr/bin/python

import sys, re

file="ftplugin/tex_atp.vim"
newstamp=sys.argv[1]
version =sys.argv[2]

file_o=open(file, "r")
file_l=file_o.readlines()
i=0
t=0
for line in file_l:
    i+=1
    if re.match('\s*"\s+Time\s+Stamp:', line):
        file_l[i-1]='" Time Stamp: '+newstamp+"\n"
        t+=1
    elif re.match('\s*let\s+(g:)?loaded_AutomaticLatexPlugin\s*=', line):
        file_l[i-1]='let g:loaded_AutomaticLatexPlugin = "'+version+"\"\n"
        t+=1
    if t== 2:
        break
file_o.close()
file_o=open(file, "w")
file_o.write("".join(file_l))
file_o.close()
