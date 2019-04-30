#!/bin/bash

# First run the html script and pipe its output to resume.js
PYHTML="/home/rutrum/workdb/genHTMLresume.py"
JSDEST="/home/rutrum/site/script/resume.js"
python3 $PYHTML > $JSDEST

# Run the LATEX script and pipe output to temp
PYLATEX="/home/rutrum/workdb/genLATEXresume.py"
TEXDEST="/tmp/resume.tex"
python3 $PYLATEX > $TEXDEST

# Compile latex
cd /tmp
pdflatex $TEXDEST
cp /tmp/resume.pdf /home/rutrum/site/resources/DavidPurdumResume.pdfs

# Now commit the changes and push to github
SITEDIR="/home/rutrum/site"
git -C $SITEDIR add /home/rutrum/site
git -C $SITEDIR commit -m "Update resume."
git -C $SITEDIR push