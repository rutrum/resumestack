#!/bin/bash

# Move the pdf to zola-site repository
PDF_SRC="/home/rutrum/repo/resumestack/resume/DavidPurdumResume.pdf"
SITE_STATIC="/home/rutrum/repo/zola-site/static/DavidPurdumResume.pdf"
cp $PDF_SRC $SITE_STATIC