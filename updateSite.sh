#!/bin/bash

COMMITMSG="Update resume."
if [[ $# -eq 1 ]]; then
    COMMITMSG="$1"
fi

# First run the html script and pipe its output to resume.js
PYHTML="/home/rutrum/repo/resumestack/genHTMLresume.py"
JSDEST="/home/rutrum/repo/site/script/resume.js"
python3 $PYHTML > $JSDEST

# Run the LATEX script and pipe output to temp
PYLATEX="/home/rutrum/repo/resumestack/genLATEXresume.py"
TEXDEST="/tmp/resume.tex"
python3 $PYLATEX > $TEXDEST

# Compile latex
cd /tmp
pdflatex $TEXDEST
cp /tmp/resume.pdf /home/rutrum/repo/site/resources/DavidPurdumResume.pdf

# Now commit the changes and push to github
SITEDIR="/home/rutrum/repo/site"
git -C $SITEDIR add /home/rutrum/repo/site
git -C $SITEDIR commit -m "$COMMITMSG"
git -C $SITEDIR push