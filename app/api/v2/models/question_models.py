import datetime
question_record = []
voting_record =[]

class QuestionRecords():
    def __init__(self):
        self.rec  = question_record


    def save(self, meetup_id, question):
        data = {
        "question_id": len(question_record) + 1,
        "meetup_id": meetup_id,
        "posted-on": datetime.datetime.now(),
        "question": question
        }
        question_record.append(data)
        return question_record

class VotingRecord():
    def __init__(self):
        self.rec = voting_record

    def locate(self, id):
        res = None
        for item in self.rec:
            if item['question_id'] == id:
                res = item
        return res

    def save(self, id, vote):

        data = {
            "question_id" : id,
            "upvotes" : 0,
            "downvotes" : 0,
            "voted_on" : datetime.datetime.now()
        }
        #Executed when the vote parsed is True

        if vote:
            data['upvotes'] = data['upvotes'] + 1

        #Executed when the vote parsed is True

        else:
            data['downvotes'] = data['downvotes'] + 1
        self.rec.append(data)
        return self.rec

    def vote(self, id, vote):
        rec = self.locate(id)

        #checks if the voting record does exist

        if rec is not None:
            if vote == True:
                rec['upvotes'] = rec['upvotes'] + 1
            else:
                rec['downvotes'] = rec['downvotes'] -1
            return rec
        else: ### record does not exists
            res = self.save(id, vote)
        return res
