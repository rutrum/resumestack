import sys
import sqlite3

# to return dict instead of list
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def write_experience(row):
    print("### {} - {}".format(
        row["institution"],
        row["title"]
    ))
    print()
    print(row["description"])
    print()

def write_project(row):
    print("### {}".format(row["title"]))
    print()
    print(row["description"])
    print()
    
def write_education(row):
    print("### {}".format(row["institution"]))
    print()
    print(row["field"])
    print()
    print("{} GPA".format(row["gpa"]))
    print()
    print(row["description"])
    print()
    
def main():

    db = sqlite3.connect('/home/rutrum/db/work.db')
    db.row_factory = dict_factory

    print("+++")
    print("title = \"Resume\"")
    print("template = \"resume.html\"")
    print("+++")
    print()
    print("You can view my resume below or look at the [pdf](/DavidPurdumResume.pdf) version.")
    print()

    print("## Education")
    print()
    edus = db.execute("SELECT * FROM Education").fetchall()
    for edu in edus:
        write_education(edu)

    print("## Skills")
    print()

    langs = db.execute("SELECT * FROM Skills WHERE type = 'lang'").fetchall()
    langbuff = ""
    for lang in langs:
        langbuff += lang["title"] + ", "
    print(langbuff[:-2])
    print()

    softs = db.execute("SELECT * FROM Skills WHERE type = 'soft'").fetchall()
    softbuff = ""
    for soft in softs:
        softbuff += soft["title"] + ", "
    print(softbuff[:-2])
    print()

    print("## Relevant Experience")
    print()
    exps = db.execute("SELECT * FROM Experience WHERE tag <> 'other' ORDER BY start DESC").fetchall()
    for exp in exps:
        write_experience(exp)

    print("## Projects")
    print()
    projs = db.execute("SELECT * FROM Projects").fetchall()
    for proj in projs:
        write_project(proj)    

    print("## Other Experience")
    print()
    otherexps = db.execute("SELECT * FROM Experience WHERE tag == 'other' ORDER BY start DESC").fetchall()
    for exp in otherexps:
        write_experience(exp)

if __name__ == "__main__":
    main()