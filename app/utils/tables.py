class Tables():
    """ Class to create tables """
    def table_queries(self):
        users="""CREATE TABLE IF NOT EXISTS users
        (
        Id  SERIAL PRIMARY KEY ,
        FirstName char(50) NOT NULL,
        LastName char(50) NOT NULL,
        OtherName char(50) NOT NULL,
        Email char(50) NOT NULL,
        Password char(250) NOT NULL,
        PhoneNumber char(10) NOT NULL,
        IsAdmin  BOOL ,
        RegisteredOn TIMESTAMP
        )"""
        meetups="""CREATE TABLE IF NOT EXISTS meetups
        (
        Id  SERIAL NOT NULL UNIQUE ,
        U_id INTEGER REFERENCES users(Id),
        Title char(50) NOT NULL,
        Description char(50) NOT NULL,
        Venue char(32) NOT NULL,
        Date char(32) NOT NULL,
        PostedOn TIMESTAMP,
        Tags char(25) NOT NULL,
        PRIMARY KEY (Id, U_id)
        )"""
        questions = """CREATE TABLE IF NOT EXISTS questions
        (
        Id  SERIAL,
        M_id INTEGER REFERENCES meetups(Id),
        U_id INTEGER REFERENCES users(Id),
        Question char(50) NOT NULL,
        Votes INTEGER,
        PostedOn TIMESTAMP,
        PRIMARY KEY (Id, M_id)
        )"""

        self.query = [users,meetups,questions]
        return self.query
