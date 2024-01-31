class Review:
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f'{self.user.name} rated this course {self.rating} and said: {self.comment}'