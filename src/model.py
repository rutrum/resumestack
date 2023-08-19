import sqlite3
import datetime

class ResumeData:
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __init__(self):
        db = sqlite3.connect('/mnt/barracuda/data/work.db')
        db.row_factory = ResumeData.dict_factory

        self.me = db.execute("SELECT * FROM Persons WHERE name='David Purdum'").fetchone()

        self.fetch_publications(db)
        self.fetch_research(db)
        self.fetch_experience(db)
        self.fetch_presentations(db)
        self.fetch_education(db)
        self.fetch_skills(db)
        self.fetch_awards(db)
        self.fetch_projects(db)

    def fetch_projects(self, db):
        self.projects = db.execute("SELECT * FROM Projects WHERE show == True ORDER BY id DESC").fetchall()

        for proj in self.projects:
            if proj["url"]:
                slashslash = proj["url"].find("//")
                proj["pretty_url"] = proj["url"]
                if slashslash != -1:
                    proj["pretty_url"] = proj["url"][slashslash + 2:]


    def fetch_publications(self, db):
        self.publications = db.execute("SELECT * FROM Publications").fetchall()

        for pub in self.publications:
            date = datetime.datetime.strptime(pub["date"], "%Y-%m-%d")
            pub["pretty_date"] = datetime.datetime.strftime(date, "%B %Y")

    def fetch_awards(self, db):
        self.awards = db.execute("SELECT * FROM Awards ORDER BY date DESC").fetchall()

        for award in self.awards:
            date = datetime.datetime.strptime(award["date"], "%Y-%m-%d")
            award["pretty_date"] = datetime.datetime.strftime(date, "%B %Y")

    def fetch_presentations(self, db):
        self.presentations = db.execute("SELECT * FROM Presentations ORDER BY date DESC").fetchall()

        for pres in self.presentations:
            date = datetime.datetime.strptime(pres["date"], "%Y-%m-%d")
            pres["pretty_date"] = datetime.datetime.strftime(date, "%B %Y")
            pres["year"] = datetime.datetime.strftime(date, "%Y")

    def fetch_experience(self, db):
        self.experience = db.execute("SELECT *, julianday(end) - julianday(start) AS days FROM Experience ORDER BY priority DESC, end DESC").fetchall()

        # Add keys for formatted days.  Turn YYYY-MM-DD into Month YYYY.
        # Key pretty_date will be a tuple with one or two elements
        for exp in self.experience:
            pretty_start = None
            if exp["start"]:
                date = datetime.datetime.strptime(exp["start"], "%Y-%m-%d")
                pretty_start = datetime.datetime.strftime(date, "%B %Y")

            pretty_end = "Present"
            if exp["end"]:
                date = datetime.datetime.strptime(exp["end"], "%Y-%m-%d")
                pretty_end = datetime.datetime.strftime(date, "%B %Y")

            exp["pretty_start"] = pretty_start
            exp["pretty_end"] = pretty_end

            days = exp["days"]
            if pretty_start == pretty_end:
                exp["pretty_date"] = (pretty_start, )
            elif days and days < 100 and "May" in pretty_start and "August" in pretty_end:
                exp["pretty_date"] = ("Summer " + pretty_start.split(" ")[1], )
            else:
                exp["pretty_date"] = (pretty_start, pretty_end)

    def fetch_education(self, db):
        self.education = db.execute("SELECT * FROM Education ORDER BY start DESC").fetchall()

        # Construct a formatted date for education: YYYY-MM-DD => Month YYYY
        for edu in self.education:
            date = datetime.datetime.strptime(edu["start"], "%Y-%m-%d")
            edu["pretty_start"] = datetime.datetime.strftime(date, "%B %Y")
            date = datetime.datetime.strptime(edu["end"], "%Y-%m-%d")
            edu["pretty_end"] = datetime.datetime.strftime(date, "%B %Y")
            edu["pretty_date"] = datetime.datetime.strftime(date, "%B %Y")


    def fetch_research(self, db):
        self.research = db.execute("SELECT *, Persons.name as advisor FROM Research, Persons WHERE advisor_id = Persons.id").fetchall()

        for res in self.research:
            pretty_start = None
            if res["start"]:
                date = datetime.datetime.strptime(res["start"], "%Y-%m-%d")
                pretty_start = datetime.datetime.strftime(date, "%B %Y")

            pretty_end = "Present"
            if res["end"]:
                date = datetime.datetime.strptime(res["end"], "%Y-%m-%d")
                pretty_end = datetime.datetime.strftime(date, "%B %Y")

            if pretty_start == pretty_end:
                res["pretty_date"] = (pretty_start, )
            else:
                res["pretty_date"] = (pretty_start, pretty_end)


    def fetch_skills(self, db):
        skills = db.execute("SELECT * FROM Skills ORDER BY weight DESC").fetchall()

        self.skills = {}
        self.skills["language"] = list(map(
            lambda skill: skill["title"],
            filter(
                lambda skill: skill["class"] == "lang",
                skills
            )
        ))

        self.skills["library"] = list(map(
            lambda skill: skill["title"],
            filter(
                lambda skill: skill["class"] == "lib",
                skills
            )
        ))

        self.skills["software"] = list(map(
            lambda skill: skill["title"],
            filter(
                lambda skill: skill["class"] == "soft",
                skills
            )
        ))

if __name__ == "__main__":
    data = ResumeData()
    print(data.me, data.experience)
