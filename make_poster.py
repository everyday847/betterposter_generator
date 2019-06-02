#!/usr/bin/env python3

import sys
import os

def image_insert(line):
    """
    For a line containing a filename, insert LaTeX that places that image.
    TODO: formatting directives; parse out line.
    """
    return "\\includegraphics[width=\\textwidth]{{{}}}".format(line)

def line_broken(txt):
    """
    The summary line needs line breaks pretty frequently, say 35c. Wait for
    the end of a word to do it. Also replace _ with \textbf
    """

    finaltxt = ""

    i = 0
    inside_uscore = False
    for c in txt:
        if c != '_': i += 1
        
        if i > 35 and c == ' ':
            i = 0
            finaltxt += '\n\\\\'
        elif c == '_':
            if inside_uscore:
                inside_uscore = False
                finaltxt += '}'
            else:
                inside_uscore = True
                finaltxt += '\\textbf{'
        else:
            finaltxt += c
    return finaltxt

def latex_escape(txt):
    """
    For now, just replaces % with \% 
    """
    return txt.replace('%', '\%')

files = sys.argv[1:]

# text:
template_text = None
#with open("{}/template/template.tex".format(os.path.realpath(__file__).replace(__file__, ''))) as f:
with open("{}/template/template.tex".format(os.path.realpath(__file__).replace(__file__.split('/')[-1], ''))) as f:
    template_text = f.read()

#print(template_text)
# OK, open each file in turn

left_insertions, right_insertions = "", ""
for fn in files:
    # if this is some text, insert it.
    with open(fn) as f:
        if 'summary' in fn:
            # special named file for the summary line
            summary = line_broken(f.read())
        for line in f:
            if line[0] == 'L':
                line = line[1:]
                if ".png" in line:
                    #print(image_insert(line.strip()))
                    left_insertions += image_insert(line.strip()) + '\n'
                elif ".txt" in line:
                    #with open(line.strip()) as g: print(line.read())
                    with open(line.strip()) as g: left_insertions += latex_escape(g.read()) + '\n'
                else:
                    #print(line.strip())
                    left_insertions += line.strip() + '\n'
            elif line[0] == 'R':
                line = line[1:]
                if ".png" in line:
                    #print(image_insert(line.strip()))
                    right_insertions += image_insert(line.strip()) + '\n'
                elif ".txt" in line:
                    #with open(line.strip()) as g: print(line.read())
                    with open(line.strip()) as g: right_insertions += latex_escape(g.read()) + '\n'
                else:
                    #print(line.strip())
                    right_insertions += line.strip() + '\n'

print(template_text.replace("TEMPLATE_LEFT_INSERT", left_insertions).replace("TEMPLATE_RIGHT_INSERT", right_insertions)
        .replace("TEMPLATE_SUMMARY", summary))

