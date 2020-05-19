import model

# Print the latex format of data to the console
def format(data):
    print(r"\documentclass{article}")
    print(r"\usepackage{/home/rutrum/repo/resumestack/src/resumestyle}")
    print(r"\begin{document}")
    print()
    write_title(data.me)
    print()
    write_experience(data.experience)
    print()
    write_skills(data.skills)
    print()
    write_projects(data.projects)
    print()
    write_education(data.education)
    print()
    print(r"\end{document}")

def write_header(title):
    print(r"\header{{{}}}".format(title))
    print()

def write_title(me):
    print(r"\bigtitle{{David Purdum}}{{ {} \\ {} \\ {} \\ {} }}".format(
        me["email"], 
        me["cell"].replace("-", r"\,-\,").replace(")", r")\ "), 
        me["github"], 
        me["linkedin"])
    )

def write_education(education):
    write_header("Education")
    for edu in education:

        majors = r" $\cdot$ ".join(list(map(lambda x: x.strip() + " Major", edu["majors"].split(","))))
        minors = r" $\cdot$ ".join(list(map(lambda x: x.strip() + " Minor", edu["minors"].split(","))))

        print(r"\entry{{{}}}{{{}}}{{{}}}{{{} \\ {}}}".format(
            edu["degree"],
            edu["institution"],
            "Graduated " + edu["pretty_date"],
            majors,
            minors
        ))

def write_skills(skills):
    write_header("Skills")

    # Change C# to C\#
    for category in skills:
        skills[category] = list(map(lambda skill: skill.replace("#", r"\#"), skills[category]))

    print(r"\simpleentry{{Proficient}}{{{}}}".format(
        r" $\cdot$ ".join(skills["proficient"]))
    )
    print()
    print(r"\simpleentry{{Familiar}}{{{}}}".format(
        r" $\cdot$ ".join(skills["familiar"]))
    )
    print()
    print(r"\simpleentry{{Technologies}}{{{}}}".format(
        r" $\cdot$ ".join(skills["software"]))
    )
    print()

def write_experience(experience):
    write_header("Experience")

    for exp in filter(lambda exp: exp["tag"] != "other", experience):
        if len(exp["pretty_date"]) == 1:
            time = exp["pretty_date"][0]
        else:
            time = r"\timeperiod{{{}}}{{{}}}".format(exp["pretty_date"][0], exp["pretty_date"][1])
        
        print(r"\entry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            exp["title"],
            exp["institution"],
            time, 
            exp["description"].replace(" n ", " $n$ ")
        ))
        print()

def write_projects(projects):
    write_header("Projects")

    for proj in projects:
        print(r"\simpleentry{{{}}}{{{}}}".format(
            proj["title"],
            proj["description"]
        ))
        print()
            
if __name__ == "__main__":
    data = model.ResumeData()
    format(data)

'''
def list_skills(skills, width):
    skillstr = ""
    i = 0
    for skill in skills:
        skill["title"] = skill["title"].replace("#", r"\#")
        if i == 0:
            skillstr += "\\\\%s" % skill["title"]
        else:
            skillstr += " $\\cdot$ %s" % skill["title"]
        i = (i + 1) % width
    return skillstr[2:]
'''