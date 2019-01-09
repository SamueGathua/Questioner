import datetime
voting_record = []

class VotingRecord():
    def __init__(self):
        self.rec  = voting_record

    def save(self, question_id, vote):
        data = {
        "vote_id": len(voting_record) + 1,
        "question_id": question_id,
        "voted-on": datetime.datetime.now(),
        "vote": vote
        }
        voting_record.append(data)
        return voting_record
