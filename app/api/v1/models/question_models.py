import datetime
question_record = []

class QuestionRecord():
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
