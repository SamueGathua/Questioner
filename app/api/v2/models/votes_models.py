import datetime
from psycopg2.extras import RealDictCursor

from ....utils.dbconnect import init_db

class VotesRecords():
        def __init__(self):
            self.db  = init_db()

        def save_upvote(self, q_id, data):
            query = "UPDATE questions  set votes = votes +1 WHERE id = '{}'".format(q_id)
            save = self.db
            cur = save.cursor()
            cur.execute(query)
            save.commit()
            return data

        def save_downvote(self,q_id, data):
            query = "UPDATE questions  set votes = votes -1 WHERE id = '{}'".format(q_id)
            save = self.db
            cur = save.cursor()
            cur.execute(query)
            save.commit()
            return data
