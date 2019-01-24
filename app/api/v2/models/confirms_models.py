import datetime
from psycopg2.extras import RealDictCursor

from ....utils.dbconnect import init_db
from .base_models import User

class ConfirmRecords():
        def __init__(self):
            self.db  = init_db()
            self.get_id= User()

        def save(self,m_id,confirm,author):
            data = {
            "meetup_id": m_id,
            "user_id":self.get_id.get_user_details(author),
            "posted-on": datetime.datetime.now(),
            "confirm": confirm
            }
            query = """INSERT INTO confirms(PostedOn, M_id, U_id, Confirm)
            VALUES ('%s', '%s','%s', '%s');""" % \
            (data['posted-on'],data['meetup_id'], data['user_id'], data['confirm'])
            save = self.db
            cur = save.cursor()
            cur.execute(query)
            save.commit()
            return data
