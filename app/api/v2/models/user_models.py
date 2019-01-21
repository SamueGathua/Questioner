import datetime
from ....utils.dbconnect import init_db


class UserRecords():
    def __init__(self):
        self.db = init_db()

    def save(self, fname,lname, email, password):
        registered_on= datetime.datetime.now()
        data = {
        "registered_on":registered_on,
        "fname": fname,
        "lname": lname,
        "email": email,
        "password" :password

        }
        query = """INSERT INTO users(FirstName, LastName, Email, Password,RegisteredOn)
        VALUES ('%s', '%s', '%s', '%s','%s');""" % \
        (data['fname'], data['lname'], data['email'], data['password'], data['registered_on'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data
