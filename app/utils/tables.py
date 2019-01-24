class Tables():
    """ Class to create tables """
    def table_queries(self):
        users="""CREATE TABLE IF NOT EXISTS users
        (
        Id  SERIAL PRIMARY KEY ,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR (50) NOT NULL,
        OtherName VARCHAR(50) NOT NULL,
        Email VARCHAR(50) NOT NULL,
        Password VARCHAR(250) NOT NULL,
        PhoneNumber VARCHAR(10) NOT NULL,
        IsAdmin  BOOL ,
        RegisteredOn TIMESTAMP
        )"""
        meetups="""CREATE TABLE IF NOT EXISTS meetups
        (
        Id  SERIAL NOT NULL UNIQUE ,
        U_id INTEGER REFERENCES users(Id),
        Title VARCHAR(50) NOT NULL,
        Description VARCHAR(50) NOT NULL,
        Venue VARCHAR(32) NOT NULL,
        Date VARCHAR(32) NOT NULL,
        PostedOn TIMESTAMP,
        Tags VARCHAR (25) NOT NULL,
        PRIMARY KEY (Id, U_id)
        )"""
        questions = """CREATE TABLE IF NOT EXISTS questions
        (
        Id  SERIAL PRIMARY KEY,
        M_id INTEGER REFERENCES meetups(Id) ON DELETE CASCADE,
        U_id INTEGER REFERENCES users(Id),
        Question VARCHAR (50) NOT NULL,
        Votes INTEGER,
        PostedOn TIMESTAMP,
        UNIQUE (Id, M_id)
        )"""
        confirms = """CREATE TABLE IF NOT EXISTS confirms
        (
        Id  SERIAL,
        M_id INTEGER REFERENCES meetups(Id) ON DELETE CASCADE,
        U_id INTEGER REFERENCES users(Id),
        Confirm VARCHAR (50) NOT NULL,
        PostedOn TIMESTAMP,
        PRIMARY KEY (Id, M_id)
        )"""
        comments = """CREATE TABLE IF NOT EXISTS comments
        (
        Id  SERIAL PRIMARY KEY,
        Q_id INTEGER REFERENCES questions(Id),
        U_id INTEGER REFERENCES users(Id),
        Comment VARCHAR (50) NOT NULL,
        PostedOn TIMESTAMP,
        UNIQUE (Id, Q_id)
        )"""



        self.query = [users,meetups,questions,confirms,comments]
        return self.query
