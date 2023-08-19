# Generate all possible outputs
all:
   just pdf resume 
   just pdf cv 
   just txt resume > target/david_purdum_resume.txt

latex DOCTYPE="resume":
    python3 src/generate.py latex {{DOCTYPE}}

md DOCTYPE="resume":
    python3 src/generate.py md {{DOCTYPE}}

txt DOCTYPE="resume":
    python3 src/generate.py txt {{DOCTYPE}} 

watch DOCTYPE="resume":
    watchexec -i target -- just pdf {{DOCTYPE}}

pdf DOCTYPE="resume":
    python3 src/generate.py latex {{DOCTYPE}} > target/david_purdum_{{DOCTYPE}}.tex
    pdflatex -halt-on-error -output-directory target target/david_purdum_{{DOCTYPE}}.tex 
    @trash target/*.log
    @trash target/*.aux
    @trash target/*.out

ats:
    python3 src/generate.py latex resume_ats > target/david_purdum_resume_ats.tex
    pdflatex -halt-on-error -output-directory target target/david_purdum_resume_ats.tex 
    @trash target/*.log
    @trash target/*.aux
    @trash target/*.out

keywords:
    python3 src/keyword_count.py

open DOCTYPE="resume":
    just pdf {{DOCTYPE}}
    zathura target/david_purdum_{{DOCTYPE}}.pdf &

clean:
    trash target/*
    trash src/__pycache__/
