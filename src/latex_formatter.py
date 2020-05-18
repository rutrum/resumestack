import model
import datetime

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

def prettyDate(str):
    if (str == None): return ""
    date = datetime.datetime.strptime(str, "%Y-%m-%d")
    return datetime.datetime.strftime(date, "%B %Y")

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
            "Graduated " + prettyDate(edu["end"]),
            majors,
            minors
        ))

def write_skills(skills):
    write_header("Skills")

    for skill in skills:
        skill["title"] = skill["title"].replace("#", r"\#")

    proficient = list(map(
        lambda skill: skill["title"], 
        filter(
            lambda skill: skill["type"] == "lang" and skill["proficiency"] == 2, 
            skills
        )
    ))

    familiar = list(map(
        lambda skill: skill["title"], 
        filter(
            lambda skill: skill["type"] == "lang" and skill["proficiency"] == 1, 
            skills
        )
    ))

    software = list(map(
        lambda skill: skill["title"], 
        filter(
            lambda skill: skill["type"] == "soft",
            skills
        )
    ))

    print(r"\simpleentry{{Proficient}}{{{}}}".format(r" $\cdot$ ".join(proficient)))
    print()
    print(r"\simpleentry{{Familiar}}{{{}}}".format(r" $\cdot$ ".join(familiar)))
    print()
    print(r"\simpleentry{{Technologies}}{{{}}}".format(r" $\cdot$ ".join(software)))
    print()

def time_period(start, end, days):
    rawstart = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = datetime.datetime.strftime(rawstart, "%B %Y")

    if end == None: 
        end = "Present"
    else:
        rawend = datetime.datetime.strptime(end, "%Y-%m-%d")
        end = datetime.datetime.strftime(rawend, "%B %Y")

    if start == end:
        return start
    elif days and days < 100 and "May" in start and "August" in end:
        return "Summer " + datetime.datetime.strftime(rawstart, "%Y")
    else:
        return r"\timeperiod{{{}}}{{{}}}".format(start, end)

    return datetime.datetime.strftime(date, "%B %Y")

def write_experience(experience):
    write_header("Experience")

    for exp in filter(lambda exp: exp["tag"] != "other", experience):
        print(r"\entry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            exp["title"],
            exp["institution"],
            time_period(exp["start"], exp["end"], exp["days"]),
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
