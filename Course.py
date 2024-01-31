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

    def addCourse(self, course):
        self.courses.append(course)

    def deleteCourse(self, course):
        self.courses.remove(course)

    def getCourses(self):
        return self.courses

    def SearchCourse(self, course):
        for i in self.courses:
            if i.name == course:
                return i
        return None

    def get_number_of_registered_students(self):
        return len(self.students)

    def get_number_of_registered_courses(self):
        return len(self.courses)

