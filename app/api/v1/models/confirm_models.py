import datetime
confirm_record = []

class ConfirmRecord():
    def __init__(self):
        self.rec  = confirm_record

    def save(self, meetup_id, confirm):
        data = {
        "confirm_id": len(confirm_record) + 1,
        "meetup_id": meetup_id,
        "posted-on": datetime.datetime.now(),
        "confirm_models": confirm
        }
        confirm_record.append(data)
        return confirm_record
