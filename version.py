#!/usr/bin/python

import sys, re, datetime
from datetime import date

# Current date stamp 
# (format dd Month YYYY, e.g. 01 January 2011):
date=date.today().strftime("%d %B %Y")

file="doc/automatic-tex-plugin.txt"
newversion=sys.argv[1]

# Read doc file (for reading):
file_o=open(file, "r")
file_l=file_o.readlines()
# Find version number:
i=0
for line in file_l:
    i+=1
    if re.match('\s+An Introduction to AUTOMATIC \(La\)TeX PLUGIN',line):
        break
# Change version number:
file_l[i-1]="	    An Introduction to AUTOMATIC (La)TeX PLUGIN (ver. "+str(newversion)+")\n"
# Change date stamp:
file_l[0]="*automatic-tex-plugin.txt* LaTeX filetype plugin	Last change: "+date+"\n"
file_o.close()
# Write file (open for overwriting):
file_o=open(file, "w")
file_o.write("".join(file_l))
file_o.close()
