import datetime

from ....utils.dbconnect import init_db
from .base_models import User

class MeetupRecords():
    def __init__(self):
        self.db = init_db()
        self.get_user = User()

    def save(self, data,author):
        postedOn= datetime.datetime.now()
        author_id = self.get_user.get_user_details(author)
        data = {
        "postedOn":postedOn,
        "user_id": author_id,
        "title": data['title'],
        "description": data['description'],
        "venue": data['venue'],
        "date" : data['date'],
        "tags": data['tags']
        }
        query = """INSERT INTO meetups(PostedOn,U_id, Title, Description,\
        Venue,Date,Tags)
        VALUES ('%s', '%s','%s', '%s', '%s','%s','%s');""" % \
        (data['postedOn'],data['user_id'], data['title'], data['description'], data['venue'],\
        data['date'], data['tags'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data
