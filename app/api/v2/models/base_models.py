from ....utils.dbconnect import init_db
class User():
    def get_user_details(self,email):
        user_data = None,
        query = "SELECT id,firstname FROM users WHERE email = '{}'".format(email)
        get_user_data = init_db()
        cursor = get_user_data.cursor()
        cursor.execute(query)
        user_data = cursor.fetchone()
        id,firstname = user_data
        if user_data:
            return id
        else:
            return False

    def check_is_admin(self,email):
        query = "SELECT id,isadmin FROM users WHERE email = '{}'".format(email)
        get_user_data = init_db()
        cursor = get_user_data.cursor()
        cursor.execute(query)
        user_data = cursor.fetchone()
        id,isadmin = user_data
        if user_data:
            return isadmin
        else:
            return False
