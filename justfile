latex:
    python3 src/latex_formatter.py

md:
    python3 src/markdown_formatter.py

pdf:
    python3 src/latex_formatter.py > target/DavidPurdumResume.tex
    pdflatex -halt-on-error -output-directory target target/DavidPurdumResume.tex 
    @trash target/*.log
    @trash target/*.aux

open pdf: pdf
    zathura target/DavidPurdumResume.pdf &

clean:
    trash target/*
