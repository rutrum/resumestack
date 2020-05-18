import sqlite3

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
        self.skills = db.execute("SELECT * FROM Skills ORDER BY weight DESC").fetchall()
        self.projects = db.execute("SELECT * FROM Projects").fetchall()
        self.experience = db.execute("SELECT *, julianday(end) - julianday(start) AS days FROM Experience ORDER BY start DESC").fetchall()

if __name__ == "__main__":
    data = ResumeData()
    print(data.me, data.experience)
