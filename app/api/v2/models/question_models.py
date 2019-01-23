import datetime
from ....utils.dbconnect import init_db
from .base_models import User

class QuestionRecords():
    def __init__(self):
        self.db  = init_db()
        self.get_user = User()

    def save(self,id, question,author):
        data = {
        "meetup_id": id,
        "user_id":self.get_user.get_user_details(author),
        "posted-on": datetime.datetime.now(),
        "question":question,
        "votes":0
        }
        query = """INSERT INTO questions(M_id, U_id, Question, Votes,PostedOn)
        VALUES ('%s','%s', '%s', '%s', '%s');""" % \
        (data['meetup_id'],data['user_id'], data['question'], data['votes'], data['posted-on'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data
