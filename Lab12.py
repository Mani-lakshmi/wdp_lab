
# sams_package - Modular Package Test

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


class Faculty:
    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name


class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title


def compile_result(student, marks_list):
    if not marks_list:
        return {
            "roll_no": student.roll_no,
            "total": 0,
            "average": 0
        }

    total = sum(marks_list)
    average = round(total / len(marks_list), 2)

    return {
        "roll_no": student.roll_no,
        "total": total,
        "average": average
    }


if __name__ == "__main__":
    s = Student("SAMS24CS014", "Ananya Rao")
    faculty = Faculty("F001", "Dr. Kavitha Menon")
    course = Course("CS501", "Database Systems")

    result = compile_result(s, [88, 76, 92])

    print("=== SAMS Modular Package Test ===")
    print(
        f"{s.name} ({s.roll_no}) -> "
        f"Total: {result['total']}, "
        f"Average: {result['average']}"
    )