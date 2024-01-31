class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.reviews = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def add_course(self, course):
        self.courses.append(course)

    def delete_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses

    def search_course(self, course):
        for i in self.courses:
            if i.name == course:
                return i
        return None

    def get_number_of_registered_students(self):
        return len(self.students)

    def get_number_of_registered_courses(self):
        return len(self.courses)


    def display_reviews(self):
         for review in self.reviews:
            print(str(review))

    def add_course_material(self, material):
        self.course_materials.append(material)

    def get_course_materials(self):
        return self.course_materials

    def schedule_live_session(self, session):
        self.live_sessions.append(session)

    def get_live_sessions(self):
        return self.live_sessions

    def get_average_rating(self):
        return self.rating_sum / self.num_ratings if self.num_ratings > 0 else 0

    def get_number_of_registered_students(self):
        return len(self.students)

    def display_reviews(self):
        for review in self.reviews:
            print(str(review))
