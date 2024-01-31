class Review:
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment

    def update_review(self, rating, comment):
        self.rating = rating
        self.comment = comment

    def set_instructor_response(self, response):
        self.instructor_response = response


