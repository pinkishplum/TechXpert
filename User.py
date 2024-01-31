class User():
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def login(self):
        print('Logged in')

    def logout(self):
        print('Logged out')

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def unenroll_course(self, course):
        self.enrolled_courses.remove(course)
        course.remove_student(self)

    def __str__(self):
        return self.name