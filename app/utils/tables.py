class Tables():
    """ Class to create tables """
    def table_queries(self):
        users = """CREATE TABLE IF NOT EXISTS users
        (
        Id  SERIAL PRIMARY KEY ,
        FirstName char(50) NOT NULL,
        LastName char(50) NOT NULL,
        Email char(50) NOT NULL,
        Password char(30) NOT NULL,
        RegisteredOn TIMESTAMP
        )"""
        meetups = """CREATE TABLE IF NOT EXISTS meetups
        (
        Id  SERIAL PRIMARY KEY ,
        Title char(50) NOT NULL,
        Description char(50) NOT NULL,
        Venue char(50) NOT NULL,
        Date char(50) NOT NULL,
        PostedOn TIMESTAMP
        )"""
        questions = """CREATE TABLE IF NOT EXISTS questions
        (
        Id  SERIAL,
        M_id INTEGER REFERENCES meetups(Id),
        Question char(50) NOT NULL,
        Votes INTEGER,
        PostedOn TIMESTAMP,
        PRIMARY KEY (Id, M_id)
        )"""
        self.query = [users,meetups,questions]
        return self.query
