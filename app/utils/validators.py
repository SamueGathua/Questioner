import re

class Validations():
    def validate_email(self, email):
        expects = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(expects, email)


    def validate_password(self, password):

        expects = "r'(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[$#@]))^.{6,12}$'"
        return re.match(expects, password)
