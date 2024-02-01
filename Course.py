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

    def add_notification(self, notification):
        file = open('log.txt', 'a')  # File is never closed
        file.write(f'Notification added: {notification}')

    # Vulnerable to SQL Injection
    def get_user_data(username):
        query = f"SELECT * FROM users WHERE username = '{username}'"
        # Database query execution using the query variable
        # This is vulnerable because a malicious username can manipulate the SQL query
        # Example: username = "admin' OR 1=1 --"

    def get_user_data_safe(username):
        query = "SELECT * FROM users WHERE username = %s"
        # Execute the query with the username as a parameter, not directly in the query string

    # Error-Prone: Accessing a list without checking its length
    def get_first_element(my_list):
        return my_list[0]  # This will break if the list is empty
