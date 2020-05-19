import model

# Print the latex format of data to the console
def format(data):
    write_experience(data.experience)
    print()
    write_skills(data.skills)
    print()
    write_projects(data.projects)
    print()
    write_education(data.education)
    print()

def big_header(title):
    print("## {}".format(title))
    print()

def small_header(title):
    print("### {}".format(title))
    print()

def write_education(education):
    big_header("Education")
    for edu in education:
        majors = ", ".join(list(map(lambda x: x.strip() + " Major", edu["majors"].split(","))))
        minors = ", ".join(list(map(lambda x: x.strip() + " Minor", edu["minors"].split(","))))

        small_header(edu["degree"] + ": " + edu["institution"])
        print(majors)
        print()
        print(minors)
        print()

def write_skills(skills):
    big_header("Skills")
    small_header("Proficient")
    print(", ".join(skills["proficient"]))
    print()
    small_header("Familiar")
    print(", ".join(skills["familiar"]))
    print()
    small_header("Technologies")
    print(", ".join(skills["software"]))
    print()

def write_experience(experience):
    big_header("Experience")

    for exp in filter(lambda exp: exp["tag"] != "other", experience):
        small_header(exp["title"] + ": " + exp["institution"])
        print(exp["description"].replace(" n ", " $n$ "))
        print()

def write_projects(projects):
    big_header("Projects")

    for proj in projects:
        small_header(proj["title"])
        print(proj["description"])
        print()
            
if __name__ == "__main__":
    data = model.ResumeData()
    format(data)
