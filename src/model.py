import sqlite3
import datetime

class ResumeData:
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __init__(self):
        db = sqlite3.connect('/home/rutrum/Dropbox/work.db')
        db.row_factory = ResumeData.dict_factory

        self.me = db.execute("SELECT * FROM Persons WHERE name='David Purdum'").fetchone()
        self.education = db.execute("SELECT * FROM Education").fetchall()
        self.projects = db.execute("SELECT * FROM Projects").fetchall()
        self.experience = db.execute("SELECT *, julianday(end) - julianday(start) AS days FROM Experience ORDER BY start DESC").fetchall()

        for edu in self.education:
            date = datetime.datetime.strptime(edu["end"], "%Y-%m-%d")
            edu["pretty_date"] = datetime.datetime.strftime(date, "%B %Y")

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

            days = exp["days"]
            if pretty_start == pretty_end:
                exp["pretty_date"] = (pretty_start, )
            elif days and days < 100 and "May" in pretty_start and "August" in pretty_end:
                exp["pretty_date"] = ("Summer " + pretty_start.split(" ")[1], )
            else:
                exp["pretty_date"] = (pretty_start, pretty_end)

        # Add key for skill lists
        skills = db.execute("SELECT * FROM Skills ORDER BY weight DESC").fetchall()

        self.skills = {}
        self.skills["proficient"] = list(map(
            lambda skill: skill["title"], 
            filter(
                lambda skill: skill["type"] == "lang" and skill["proficiency"] == 2, 
                skills
            )
        ))

        self.skills["familiar"] = list(map(
            lambda skill: skill["title"], 
            filter(
                lambda skill: skill["type"] == "lang" and skill["proficiency"] == 1, 
                skills
            )
        ))

        self.skills["software"] = list(map(
            lambda skill: skill["title"], 
            filter(
                lambda skill: skill["type"] == "soft",
                skills
            )
        ))

if __name__ == "__main__":
    data = ResumeData()
    print(data.me, data.experience)
