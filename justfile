latex:
    python3 src/latex_formatter.py

pdf:
    python3 src/latex_formatter.py > target/DavidPurdumResume.tex
    pdflatex -halt-on-error -output-directory target target/DavidPurdumResume.tex 
    @trash target/*.log
    @trash target/*.aux

clean:
    trash target/*
