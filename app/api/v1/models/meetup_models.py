import datetime

meetup_record = []

class MeetupRecords():
    def __init__(self):
        self.rec = meetup_record

    def save(self, title, description, host, venue, date):
        data = {
        "id": len(meetup_record) + 1,
        "postedOn":datetime.datetime.now(),
        "title": title,
        "description": description,
        "host": host,
        "venue": venue,
        "date" : date
        }
        meetup_record.append(data)
        return meetup_record

    def get_records(self):
        return meetup_record

    def find(self, id):
        result = False
        for meetup in meetup_record:
            if meetup['id'] == id:
                return meetup
        return result
