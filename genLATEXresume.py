import sys
import sqlite3
import datetime
import re

# to return dict instead of list
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def prettyDate(str):
    if (str == None): return ""
    date = datetime.datetime.strptime(str, "%Y-%m-%d")
    return datetime.datetime.strftime(date, "%B %Y")

def write_preamble():
    print("\\documentclass{article}")
    print()
    print("\\usepackage{/home/rutrum/Dropbox/resume/resumestyle}")
    print()
    print("\\begin{document}")
    print()

def write_final():
    print("\\end{document}")

def write_header(str):
    print("\header {" + str + "}\n")

def write_title():
    print("""\\bigtitle
    {David Purdum}
    {
        purdum41@gmail.com \\\\
        (317) 760\\,-\\,9416 \\\\
        github.com/rutrum \\\\
        linkedin.com/davidpurdum
    }
    """)

def write_education(db):
    write_header("Education")


    edus = db.execute("SELECT * FROM Education").fetchall()
    for edu in edus:
        # Replace commas with cdots
        majors = re.sub(",", " $\\cdot$", edu["field"])
        description = re.sub(",", " $\\cdot$", edu["description"])
        print("""\\entry
    {%s}
	{\\textit{%s}}
	{}
	{
		%s \\\\ 
		%s \smallvspace \\\\
		\\textit{%s}
	}
    """ % (
        edu["institution"],
        prettyDate(edu["end"]) + " Expected",
        majors,
        str(edu["gpa"]) + " GPA",
        description
    ))

def write_skills(db):
    write_header("Skills")

    langs = db.execute("SELECT * FROM Skills WHERE type = 'lang'").fetchall()
    langstr = ""
    i = 0
    for lang in langs:
        lang["title"] = re.sub("#", "\\#", lang["title"])
        if i == 0:
            langstr += "\\\\%s" % lang["title"]
        elif i == 1:
            langstr += " $\\cdot$ %s" % lang["title"]
        elif i == 2:
            langstr += " $\\cdot$ %s" % lang["title"]
        i = (i + 1) % 3

    softs = db.execute("SELECT * FROM Skills WHERE type = 'soft'").fetchall()
    softstr = ""
    for soft in softs:
        if i == 0:
            softstr += "\\\\%s" % soft["title"]
        elif i == 1:
            softstr += " $\\cdot$ %s" % soft["title"]
        elif i == 2:
            softstr += " $\\cdot$ %s" % soft["title"]
        i = (i + 1) % 3
    
    print("""\\skillsentry
	{%s}
	{%s}
    """ % (
        langstr[2:], softstr[2:]
    ))

def write_relavant_exp(db):
    write_header("Relavant Experience")
    exps = db.execute("SELECT * FROM Experience WHERE tag <> 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

def write_projects(db):
    write_header("Projects")
    projs = db.execute("SELECT * FROM Projects").fetchall()
    for proj in projs:
        print("""\\simpleentry
	{%s}
	{%s}
    """ % (
        proj["title"],
        proj["description"]
    ))

def write_other_exp(db):
    write_header("Other Experience")
    exps = db.execute("SELECT * FROM Experience WHERE tag = 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

def write_experience(exp):
    start = prettyDate(exp["start"])
    end = prettyDate(exp["end"])
    exp["description"] = re.sub(" n ", " $n$ ", exp["description"])
    if (end == ""):
        end = "Present"
    time = "{\\timeperiod{%s}{%s}}" % (start, end)
    if start == end:
        time = "{%s}" % start
    print("""\\entry
	{%s}
	{%s}
	{%s}
	{%s}
    """ % (
        exp["title"],
        exp["institution"],
        time,
        exp["description"]
    ))
    
def main():

    db = sqlite3.connect('/home/rutrum/db/work.db')
    db.row_factory = dict_factory

    write_preamble()
    write_title()

    write_education(db)
    write_skills(db)
    write_relavant_exp(db)
    write_projects(db)
    write_other_exp(db)

    write_final()

if __name__ == "__main__":
    main()