import datetime
from psycopg2.extras import RealDictCursor

from ....utils.dbconnect import init_db
from .base_models import User

class MeetupRecords():
    def __init__(self):
        self.db = init_db()
        self.get_data = User()

    def save(self, data,author):

         data = {
         "postedOn":datetime.datetime.now(),
         "user_id": self.get_data.get_user_details(author),
         "title": data['title'],
         "description": data['description'],
         "venue": data['venue'],
         "date" : data['date'],
         "tags": data['tags']
         }
         query = """INSERT INTO meetups(PostedOn,U_id, Title, \
         Description,Venue,Date,Tags)
         VALUES ('%s', '%s','%s', '%s', '%s','%s','%s');""" % \
         (data['postedOn'],data['user_id'], data['title'], data['description'], data['venue'],\
         data['date'], data['tags'])

         save = self.db
         cur = save.cursor()
         cur.execute(query)
         save.commit()
         return data

    def get_all_meetup_records(self):
       query = """ SELECT * FROM meetups"""
       cur = self.db.cursor(cursor_factory=RealDictCursor)
       cur.execute(query)
       return cur.fetchall()

    def get_specific_meetup_record(self, id):
         query = "SELECT * FROM meetups WHERE id = '{}'".format(id)
         cur = self.db.cursor(cursor_factory=RealDictCursor)
         cur.execute(query)
         data =cur.fetchall()
         if data:
             return data
         else:
             return None

    def delete_specific_meetups(self,id):
        query = " DELETE FROM meetups WHERE id={};".format(id)
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        return True
