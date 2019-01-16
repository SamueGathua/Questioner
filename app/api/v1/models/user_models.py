import datetime

signup_record = []

class UserRecords():
    def __init__(self):
        self.rec = signup_record

    def save(self, fname,lname, email, password):
        data = {
        "id": len(signup_record) + 1,
        "RegisteredOn":datetime.datetime.now(),
        "fname": fname,
        "lname": lname,
        "email": email,
        "password" :password

        }
        signup_record.append(data)
        return signup_record

    def login_user(self, email, password):

        user = None
        authentication = False
        for record in self.rec:
            #checks whether the email provided does exist in the users records
            if record['email'] == email:
                user = record
                break
        if user is not None:
            #Checks that the password provided matches the one in the users records
            if user['password'] == password:
                authentication = 'Success'
            else:
                authentication = 'Fail'
        return authentication
