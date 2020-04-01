#!/bin/bash

PROJECTDIR="/home/rutrum/repo/resumestack/"
SAVE_DIR=$PROJECTDIR"resume/"

# Construct the resume tex, then convert to pdf
TO_TEX=$PROJECTDIR"src/genLATEXresume.py"
TEX_DEST="/tmp/resume.tex"
PDF_DEST="/tmp/resume.pdf"
python3 $TO_TEX > $TEX_DEST
cd /tmp
pdflatex $TEX_DEST
cp $TEX_DEST $SAVE_DIR"DavidPurdumResume.tex"
cp $PDF_DEST $SAVE_DIR"DavidPurdumResume.pdf"

# Construct the markdown for zola-site repository
TO_MD=$PROJECTDIR"src/genMDresume.py"
SITE_RESUME="/home/rutrum/repo/zola-site/content/resume/_index.md"
python3 $TO_MD > $SITE_RESUME

# Move the pdf to zola-site repository
SITE_STATIC="/home/rutrum/repo/zola-site/static/DavidPurdumResume.pdf"
cp $PDF_DEST $SITE_STATIC

# COMMITMSG="Update resume."
# if [[ $# -eq 1 ]]; then
#     COMMITMSG="$1"
# fi

# # First run the html script and pipe its output to resume.js
# PYHTML="/home/rutrum/repo/resumestack/genHTMLresume.py"
# JSDEST="/home/rutrum/repo/site/script/resume.js"
# python3 $PYHTML > $JSDEST

# # Run the LATEX script and pipe output to temp
# PYLATEX="/home/rutrum/repo/resumestack/src/genLATEXresume.py"
# TEXDEST="/tmp/resume.tex"
# python3 $PYLATEX > $TEXDEST

# # Compile latex
# cd /tmp
# pdflatex $TEXDEST
# cp /tmp/resume.pdf /home/rutrum/repo/site/resources/DavidPurdumResume.pdf

# Now commit the changes and push to github
# SITEDIR="/home/rutrum/repo/site"
# git -C $SITEDIR add /home/rutrum/repo/site
# git -C $SITEDIR commit -m "$COMMITMSG"
# git -C $SITEDIR push