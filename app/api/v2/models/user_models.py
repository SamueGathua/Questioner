import datetime
from ....utils.dbconnect import init_db
signup_record = []

class UserRecords():
    def __init__(self):
        self.db = init_db()

    def save(self, fname,lname, email, password):
        data = {
        "id": len(signup_record) + 1,
        "RegisteredOn":datetime.datetime.now(),
        "fname": fname,
        "lname": lname,
        "email": email,
        "password" :password

        }
        query = """INSERT INTO users(FirstName, LastName, Email, Password)
        VALUES ('%s', '%s', '%s', '%s');""" % \
        (data['fname'], data['lname'], data['email'], data['password'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data

    
