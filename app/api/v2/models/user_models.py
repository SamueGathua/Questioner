import datetime
from werkzeug.security import generate_password_hash
from ....utils.dbconnect import init_db

class UserRecords():
    def __init__(self):
        self.db = init_db()

    def save(self, data):


        data = {
        "registered_on":datetime.datetime.now(),
        "firstname": data['firstname'],
        "lastname": data['lastname'],
        "othername": data['othername'],
        "email": data['email'],
        "phonenumber":data['phonenumber'],
        "password":generate_password_hash( data['password'],method='pbkdf2:sha256', salt_length=8),
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
        user_data = None,
        query = "SELECT password, email FROM users WHERE email = '{}'".format(email)
        get_user_data = init_db()
        cursor = get_user_data.cursor()
        cursor.execute(query)
        user_data = cursor.fetchone()
        if user_data == None:
            return False

        return user_data
