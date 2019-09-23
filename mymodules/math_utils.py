from mymodules.models import Student

def average_grade(roster):
    grades = [Student.student_grade for Student in roster]
    return sum(grades) / len(grades)