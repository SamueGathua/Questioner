import datetime
from psycopg2.extras import RealDictCursor

from ....utils.dbconnect import init_db
from .base_models import User

class CommentsRecords():
        def __init__(self):
            self.db  = init_db()
            self.get_id= User()

        def save_comments(self,q_id,comment,author):
            data = {
            "question_id": q_id,
            "user_id":self.get_id.get_user_details(author),
            "posted-on": datetime.datetime.now(),
            "comment": comment
            }
            query = """INSERT INTO comments(PostedOn, Q_id, U_id, Comment)
            VALUES ('%s', '%s','%s', '%s');""" % \
            (data['posted-on'],data['question_id'], data['user_id'], data['comment'])
            save = self.db
            cur = save.cursor()
            cur.execute(query)
            save.commit()
            return data
