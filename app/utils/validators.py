import re

class Validations():


    def validate_email(self, email):
        expects = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(expects, email)


    def validate_password(self, password):

        valid = "^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})"
        return re.match(valid, password)
