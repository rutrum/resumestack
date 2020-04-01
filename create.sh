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

# Construct markdown resume for zola-site
TO_MD=$PROJECTDIR"src/genMDresume.py"
python3 $TO_MD > $SAVE_DIR"_index.md"