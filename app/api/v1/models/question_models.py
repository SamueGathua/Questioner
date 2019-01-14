import datetime
question_record = []
voting_record =[]

class QuestionRecords():
    def __init__(self):
        self.rec  = question_record
        self.rec = voting_record

    def save(self, meetup_id, question):
        data = {
        "question_id": len(question_record) + 1,
        "meetup_id": meetup_id,
        "posted-on": datetime.datetime.now(),
        "question": question
        }
        question_record.append(data)
        return question_record

class VotingRecords():
    def save(self, question_id, vote):
        data = {
        "vote_id": len(voting_record) + 1,
        "question_id": question_id,
        "voted-on": datetime.datetime.now(),
        "vote": vote
        }
        voting_record.append(data)
        return voting_record
