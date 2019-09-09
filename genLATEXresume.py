import sys
import sqlite3
import datetime
import re

### ---------------- ###
### Helper Functions ###
### ---------------- ###

# to return dict instead of list
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Converts YYYY-MM-DD -> Month YYYY
def prettyDate(str):
    if (str == None): return ""
    date = datetime.datetime.strptime(str, "%Y-%m-%d")
    return datetime.datetime.strftime(date, "%B %Y")

# Constructs header
def write_header(title):
    print("\header {" + title + "}\n")

# Constructs an experience
def write_experience(exp):

    description = re.sub(" n ", " $n$ ", exp["description"])
    
    start = prettyDate(exp["start"])
    end = prettyDate(exp["end"])
    if (end == ""):
        end = "Present"
        
    time = "{\\timeperiod{%s}{%s}}" % (start, end)
    if start == end:
        time = "{%s}" % start

    print("\\entry{%s}{%s}{%s}{%s}\n"
        % (exp["title"], exp["institution"], time, description) )

# Constuctions an education
def write_degree(edu):

    majors = re.sub(",", " $\\cdot$", edu["field"])
    description = re.sub(",", " $\\cdot$", edu["description"])

    print("\\entry{%s}{\\textit{%s}}{}{%s \\\\ %s \smallvspace \\\\ \\textit{%s}}\n"
        % (
            edu["institution"],
            prettyDate(edu["end"]) + " Expected",
            majors,
            str(edu["gpa"]) + " GPA",
            description
        ))

# Returns a formatted list of skills
# Each line has at most width skills
def list_skills(skills, width):
    skillstr = ""
    i = 0
    for skill in skills:
        skill["title"] = re.sub("#", "\\#", skill["title"])
        if i == 0:
            skillstr += "\\\\%s" % skill["title"]
        else:
            skillstr += " $\\cdot$ %s" % skill["title"]
        i = (i + 1) % width
    return skillstr

### ----------------------------- ###
### Resume Construction Functions ###
### ----------------------------- ###

# Packages and begin document
def write_preamble():
    print("\\documentclass{article}")
    print("\\usepackage{/home/rutrum/Dropbox/resume/resumestyle}")
    print("\\begin{document}")

# Name and contact info
def write_title(db):
    me = db.execute("SELECT * FROM Persons WHERE name='David Purdum'").fetchone()

    # Format number to add spacing
    phone = me["cell"]
    phone = re.sub("\)", ") ", phone)
    phone = re.sub("-", "\\,-\\,", phone)

    print("\\bigtitle{David Purdum}{%s \\\\ %s \\\\ %s \\\\ %s}\n"
        % (me["email"], phone, me["github"], me["linkedin"]) )

# Education history
def write_education(db):
    write_header("Education")

    edus = db.execute("SELECT * FROM Education").fetchall()
    for edu in edus:
        write_degree(edu)

# List of language and software proficiencies
def write_skills(db):
    write_header("Skills")

    langs = db.execute("SELECT * FROM Skills WHERE type = 'lang'").fetchall()
    langstr = list_skills(langs, 4)

    softs = db.execute("SELECT * FROM Skills WHERE type = 'soft'").fetchall()
    softstr = list_skills(softs, 3)
    
    print("\\skillsentry{%s}{%s}\n" 
        % (langstr[2:], softstr[2:]) )

# List of technical jobs and activities
def write_relevant_exp(db):
    write_header("Relevant Experience")
    exps = db.execute("SELECT * FROM Experience WHERE tag <> 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

# List of personal projects
def write_projects(db):
    write_header("Projects")
    projs = db.execute("SELECT * FROM Projects").fetchall()
    for proj in projs:
        print("\\simpleentry{%s}{%s}\n" 
            % (proj["title"], proj["description"]) )

# List of non-technical jobs
def write_other_exp(db):
    write_header("Other Experience")
    exps = db.execute("SELECT * FROM Experience WHERE tag = 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

# End document
def write_final():
    print("\\end{document}")

### ---- ###
### Main ###
### ---- ###

def main():

    db = sqlite3.connect('/home/rutrum/db/work.db')
    db.row_factory = dict_factory

    write_preamble()
    write_title(db)

    write_education(db)
    write_skills(db)
    write_relevant_exp(db)
    write_projects(db)
    write_other_exp(db)

    write_final()

if __name__ == "__main__":
    main()