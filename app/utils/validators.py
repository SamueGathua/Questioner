class Validations():
    def validate_meetup_keys(self, data):

        try:
            title = data['title']
            description = data['description']
            venue = data['venue']
            date = data['date']

        except KeyError:
            data = False
        return data



    def validate_confirm_attendance_keys(self, data):

        try:
            confirm = data['confirm']

        except KeyError:
            data = False
        return data
    def validate_voting_keys(self, data):

        try:
            vote = data['vote']

        except KeyError:
            data = False
        return data
