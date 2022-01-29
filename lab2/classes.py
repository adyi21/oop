"""Module docstring"""
import json



class Person():
    """Person class"""
    def __init__(self, name, ssn, address=""):
        self.name = name
        self._ssn = ssn
        self.address = address

    def set_address(self, addres):
        """Set method for address"""
        self.address = addres

    def get_ssn(self):
        """get method for ssn"""
        return self._ssn

    def __str__(self):
        """str method"""
        return f"Name: {self.name} SSN: {self._ssn} {str(self.address)}"

class Address():
    """Address class"""
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        """str method"""
        return f"Address: {self.city} {self.state} {self.country}"

class Teacher(Person):
    """teacher class"""
    @staticmethod
    def from_json(filename):
        """from json method"""
        f = open(filename, encoding="utf8")
        data = json.load(f)
        larare = Teacher(data["name"], data["ssn"], data["courses"])
        return larare

    def to_json(self):
        """to_json method"""
        x = json.dumps({"name": self.name, "ssn": self.get_ssn(),
        "courses": self.courses }, indent=4)
        return x


    def __init__(self, name, ssn, courses = None ):
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        super().__init__(name, ssn)

    def add_course(self, course):
        """add course method"""
        self.courses.append(course)

    def __str__(self):
        """str method"""
        ret_str = ", ".join(self.courses)
        return f"{super().__str__()}Courses: {ret_str}"

class Student(Person):
    """student class"""
    def __init__(self, name, ssn, courses_grades= None):
        super().__init__(name, ssn)
        if courses_grades is None:
            self.courses_grades = []
        else:
            self.courses_grades = courses_grades

    def add_course_grade(self, course, grade):
        """add course grade method"""
        self.courses_grades.append((course,grade))

    def average_grade(self):
        """average grade method"""
        grade_avg = 0
        total_no = 0
        for i in enumerate(self.courses_grades):
            if (i[1][1]) != "-":
                grade_avg += i[1][1]
                total_no += 1

        return grade_avg/(total_no)
