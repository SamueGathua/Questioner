import datetime

signup_record = []

class SignupRecords():
    def __init__(sel):
        self.rec = signup_record

    def save(self, uname, email, password):
        data = {
        "id": len(signup_record) + 1,
        "RegisteredOn":datetime.datetime.now(),
        "uname": uname,
        "email": email,
        "password" :password

        }
        signup_record.append(data)
        return signup_record
    def test_signup_post(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)
