import datetime
from ....utils.dbconnect import init_db

class UserRecords():
    def __init__(self):
        self.db = init_db()

    def save(self, data):
        registered_on= datetime.datetime.now()
        data = {
        "registered_on":registered_on,
        "firstname": data['firstname'],
        "lastname": data['lastname'],
        "othername": data['othername'],
        "email": data['email'],
        "phonenumber":data['phonenumber'],
        "password": data['password'],
        "isadmin": data['isadmin']

        }
        query = """INSERT INTO users(FirstName, LastName, OtherName,\
        Email,Password,RegisteredOn,IsAdmin,PhoneNumber)
        VALUES ('%s', '%s', '%s', '%s','%s','%s','%s','%s');""" % \
        (data['firstname'], data['lastname'], data['othername'], data['email'],\
        data['password'], data['registered_on'],data['isadmin'],data['phonenumber'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data
        
    def login_user(self, email):

        query = "SELECT * FROM users WHERE email = '{}'".format(email)
        get_user_data = init_db()
        cursor = get_user_data.cursor()
        cursor.execute(query)
        user_data = cursor.fetchone()
        return user_data
