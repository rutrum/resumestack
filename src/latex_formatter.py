def write_header(title):
    print(r"\header{{{}}}".format(title))
    print()

def write_title(me):
    print(r"\bigtitle{{David Purdum}}{{ {} \\ {} \\ \selflink{{{}}} \\ \selflink{{{}}} }}".format(
        me["email"],
        me["cell"].replace("-", r"\,-\,").replace(")", r")\ "),
        me["website"],
        me["github"],
    ))

def write_awards(awards):
    write_header("Awards and Recognition")

    for award in awards:
        print(r"\award{{{}}}{{{}}}".format(
            award["pretty_date"],
            award["name"]
        ))
        print()
    print(r"\smallvspace")

def write_publications(publications):
    write_header("Publications")

    for pub in publications:
        print(r"\publication{{{}}}{{{}}}{{{}}}{{{}}}".format(
            pub["pretty_date"] or "Work in Progress",
            pub["title"],
            pub["publication"],
            pub["authors"],
        ))

def write_research(research):
    write_header("Research")

    for res in research:
        if len(res["pretty_date"]) == 1:
            time = res["pretty_date"][0]
        else:
            time = r"\timeperiod{{{}}}{{{}}}".format(res["pretty_date"][0], res["pretty_date"][1])

        print(r"\entry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            res["field"],
            "with " + res["advisor"],
            time,
            res["description"].replace(" n ", " $n$ ")
        ))
        print()

def write_presentations(presentations):
    write_header("Presentations")

    for pres in presentations:
        print(r"\workentry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            pres["title"],
            pres["type"].capitalize(),
            pres["conference"],
            pres["pretty_date"]
        ))
        print()

def write_education(education):
    write_header("Education")
    for edu in education:

        description = ""
        if edu["majors"]:
            majors = r" $\cdot$ ".join(list(map(lambda x: x.strip() + " Major", edu["majors"].split(","))))
            description = majors
            """
            if edu["minors"]:
                minors = r" $\cdot$ ".join(list(map(lambda x: x.strip() + " Minor", edu["minors"].split(","))))
                description = r"{} \\ {}".format(majors, minors)
            else:
                description = majors
            """
        elif edu["program"]:
            description = edu["program"] + " Program"

        print(r"\entry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            edu["degree"],
            edu["institution"],
            "Graduated " + edu["pretty_date"],
            description
        ))

        print()

def write_skills(skills):
    write_header("Skills")

    # Change C# to C\#
    for category in skills:
        skills[category] = list(map(lambda skill: skill.replace("#", r"\#"), skills[category]))

    print(r"\skillentry{{Languages}}{{{}}}".format(
        r" $\cdot$ ".join(skills["language"]))
    )
    print()
    print(r"\skillentry{{Tools}}{{{}}}".format(
        r" $\cdot$ ".join(skills["software"]))
    )
    print(r"\smallvspace")
    print()

def write_experience(experience):
    write_header("Experience")

    for exp in filter(lambda exp: exp["filter"] == 1, experience):
        if len(exp["pretty_date"]) == 1:
            time = exp["pretty_date"][0]
        else:
            time = r"\timeperiod{{{}}}{{{}}}".format(exp["pretty_date"][0], exp["pretty_date"][1])

        print(r"\bulletentry{{{}}}{{{}}}{{{}}}{{{}}}".format(
            exp["title"],
            exp["institution"],
            time,
            r"\item{" + exp["description"]
                .replace(" n ", " $n$ ")
                .replace(". ", r".}\item{")
                + "}"
        ))
        print()

def write_projects(projects):
    write_header("Projects")

    for proj in projects:
        description = r"\item{" + proj["description"].replace(". ", r".}\item{") + "}"
        if proj["url"]:
            url = proj["url"].replace("_", "\\_")
            pretty_url = proj["pretty_url"].replace("_", "\\_")

            print(r"\bulletentry{{{}}}{{{}}}{{\link{{{}}}{{{}}}}}{{{}}}".format(
                proj["title"],
                "",
                url,
                pretty_url,
                description,
            ))
        else:
            print(r"\bulletsimpleentry{{{}}}{{{}}}".format(
                proj["title"],
                description,
            ))
        print()

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
