import sys
import sqlite3

# to return dict instead of list
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def tag(tag, inner):
    print("<" + tag + ">" + str(inner) + "</" + tag + ">", end="")

def write_experience(row):
    tag("h3", row["institution"] + " - " + row["title"])
    tag("p", row["description"])

def write_project(row):
    tag("h3", row["title"])
    tag("p", row["description"])
    
def write_education(row):
    tag("h3", row["institution"])
    tag("p", row["field"])
    tag("p", str(row["gpa"]) + " GPA")
    tag("p", row["description"])
    
def main():

    db = sqlite3.connect('/home/rutrum/db/work.db')
    db.row_factory = dict_factory

    print("let resumestr = \"", end="")

    tag("h2", "Education")
    edus = db.execute("SELECT * FROM Education").fetchall()
    for edu in edus:
        write_education(edu)

    tag("h2", "Skills")
    langs = db.execute("SELECT * FROM Skills WHERE type = 'lang'").fetchall()
    langbuff = ""
    for lang in langs:
        langbuff += lang["title"] + ", "
    tag("p", langbuff[:-2])
    softs = db.execute("SELECT * FROM Skills WHERE type = 'soft'").fetchall()
    softbuff = ""
    for soft in softs:
        softbuff += soft["title"] + ", "
    tag("p", softbuff[:-2])

    tag("h2", "Relevant Experience")
    exps = db.execute("SELECT * FROM Experience WHERE tag <> 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

    tag("h2", "Projects")
    projs = db.execute("SELECT * FROM Projects").fetchall()
    for proj in projs:
        write_project(proj)    

    tag("h2", "Other Experience")
    otherexps = db.execute("SELECT * FROM Experience WHERE tag == 'other' ORDER BY start DESC").fetchall()
    for exp in otherexps:
        write_experience(exp)

    print("\"", end="")

if __name__ == "__main__":
    main()