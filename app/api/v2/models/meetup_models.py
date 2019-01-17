import datetime

meetup_record = []
confirm_record = []

class MeetupRecords():
    def __init__(self):
        self.rec = meetup_record

    def save(self, title, description,venue, date):
        data = {
        "id": len(meetup_record) + 1,
        "postedOn":datetime.datetime.now(),
        "title": title,
        "description": description,
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


class ConfirmRecords():
        def __init__(self):
            self.rec  = confirm_record

        def get_confirms(self, m_id):
            return confirm_record

        def save(self, meetup_id, confirm):
            data = {
            "confirm_id": len(confirm_record) + 1,
            "meetup_id": meetup_id,
            "posted-on": datetime.datetime.now(),
            "confirm_models": confirm
            }
            confirm_record.append(data)
            return confirm_record
