
# sams_domain_model.py

class Student:
    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa
        self.enrolled_courses = []

    def enrol(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.enrolled_students.append(self)

    def display_profile(self):
        courses = ", ".join(c.code for c in self.enrolled_courses) or "None"
        print(
            f"{self.roll_no} | {self.name} | "
            f"CGPA {self.cgpa} | Courses: {courses}"
        )


class Faculty:
    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name
        self.courses_taught = []

    def assign_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)
        course.faculty = self


class Course:
    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits
        self.enrolled_students = []
        self.faculty = None


if __name__ == "__main__":
    cs501 = Course("CS501", "Database Systems", 4)
    cs502 = Course("CS502", "Operating Systems", 4)

    faculty = Faculty("F001", "Dr. Kavitha Menon")
    faculty.assign_course(cs501)

    student1 = Student("SAMS24CS014", "Ananya Rao", 8.7)
    student2 = Student("SAMS24CS015", "Rohit Verma", 8.5)

    student1.enrol(cs501)
    student1.enrol(cs502)
    student2.enrol(cs501)

    print("=== SAMS Domain Model ===")
    student1.display_profile()
    student2.display_profile()

    print("Faculty:", faculty.name)
    print("Courses taught:", ", ".join(c.code for c in faculty.courses_taught))
    print("CS501 enrolled students:", len(cs501.enrolled_students))