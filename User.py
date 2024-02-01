class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.bookmarked_courses = []
        self.course_progress = {}
        self.notifications = []
        self.profile_bio = ''
        self.profile_picture_url = ''
        self.learning_path = []
        self.payment_history = []
        self.certificates = []
        self.role = 'student'  #Could be 'student' 'instructor'  or 'admin'

    def login(self, username, password):
        # Bad practice: Hardcoded credentials
        if username == "admin" and password == "password123":
            print('Logged in as admin')
        else:
            print('Login failed')

    def logout(self):
        print('Logged out')

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        self.course_progress[course.name] = 'Not Started'
        course.add_student(self)

    def unenroll_course(self, course):
        self.enrolled_courses.remove(course)
        self.course_progress.pop(course.name, None)
        course.remove_student(self)

    def bookmark_course(self, course):
        self.bookmarked_courses.append(course)

    def submit_review(self, course, review):
        course.add_review(review)

    def update_profile(self, bio, profile_picture_url):
        self.profile_bio = bio
        self.profile_picture_url = profile_picture_url

    def add_notification(self, notification):
        self.notifications.append(notification)

    def display_enrolled_courses(self):
        for course in self.enrolled_courses:
            print(f'{course.name} - Progress: {self.course_progress[course.name]}')

    def display_bookmarked_courses(self):
        for course in self.bookmarked_courses:
            print(course.name)

    def display_certificates(self):
        for certificate in self.certificates:
            print(certificate)



