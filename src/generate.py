import sys
import latex_formatter as latex
import txt_formatter as txt
import markdown_formatter as md
import model

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
    markup = sys.argv[1].lower()
    doc_type = sys.argv[2].lower()

    data = model.ResumeData()
    if markup == "md" and doc_type == "resume":
        md_resume_format(data)
    elif markup == "latex" and doc_type == "resume":
        latex_resume_format(data)
    elif markup == "txt" and doc_type == "resume":
        txt_resume_format(data)
    #elif markup == "md" and doc_type == "cv":
    #    md_resume_format(data)
    elif markup == "latex" and doc_type == "cv":
        latex_cv_format(data)
    else:
        sys.stderr.write("Invalid markup format or document type\n")

def md_resume_format(data):
    md.write_experience(data.experience)
    print()
    md.write_skills(data.skills)
    print()
    md.write_projects(data.projects)
    print()
    md.write_education(data.education)
    print()

def latex_resume_format(data):
    print(r"\documentclass{article}")
    print(r"\usepackage{/home/rutrum/repo/resumestack/src/resumestyle}")
    print(r"\begin{document}")
    print()
    latex.write_title(data.me)
    print()
    latex.write_experience(data.experience, ["cs", "internship"])
    print()
    latex.write_skills(data.skills)
    print()
    latex.write_projects(data.projects)
    print()
    latex.write_education(data.education)
    print()
    print(r"\end{document}")

def latex_cv_format(data):
    print(r"\documentclass{article}")
    print(r"\usepackage{/home/rutrum/repo/resumestack/src/resumestyle}")
    print(r"\begin{document}")
    print()
    latex.write_title(data.me)
    print()
    latex.write_education(data.education)
    print()
    latex.write_research(data.research)
    print()
    latex.write_publications(data.publications)
    print()
    latex.write_experience(data.experience, ["cs"])
    print()
    latex.write_presentations(data.presentations)
    print()
    latex.write_projects(data.projects)
    print()
    latex.write_awards(data.awards)
    print()
    print(r"\end{document}")

def txt_resume_format(data):
    txt.write_title(data.me)
    print()
    txt.write_experience(data.experience)
    print()
    txt.write_education(data.education)
    print()
    txt.write_skills(data.skills)

if __name__ == "__main__":
    main()
