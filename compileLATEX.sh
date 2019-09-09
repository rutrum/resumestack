#!/bin/bash
# This script is for testing purposes

PYLATEX="/home/rutrum/resumestack/genLATEXresume.py"
TEXDEST="/tmp/resume.tex"
python3 $PYLATEX > $TEXDEST

cd /tmp
pdflatex $TEXDEST
zathura /tmp/resume.pdf
rm /tmp/resume.pdf # so I know it compiled correctly