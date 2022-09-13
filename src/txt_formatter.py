def write_title(me):
    print("David Purdum")
    print(me["email"])
    print(me["cell"])
    print(me["website"])
    print(me["github"])

def write_experience(experience):
    print("# Experience")
    for exp in [ e for e in experience if e["tag"] in ["cs", "internship"]]:
        print()
        print(exp["title"])
        print(exp["institution"])
        print(exp["pretty_start"], "-", exp["pretty_end"])
        print(exp["description"])

def write_skills(skills):
    print("# Skills")
    print()
    print(", ".join(skills["proficient"]))
    print(", ".join(skills["familiar"]))
    print(", ".join(skills["software"]))

def write_education(education):
    print("# Education")
    for edu in education:
        print()
        print(edu["institution"])
        print(edu["degree"])
        print(edu["pretty_start"], "-", edu["pretty_end"])
        print(edu["majors"] or edu["program"])
