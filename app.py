from mymodules.models import Student
from mymodules.math_utils import average_grade
def main():
#create 10 students, print the list of students, and print the average score of the roster
    roster = []
    #roster.append(Student("Anna", 0))
    #roster.append(Student("Andrew"))
    #roster.append(Student("John"))
    #roster.append(Student("Tom"))
    #roster.append(Student("Lisa"))
    #roster.append(Student("Tony"))
    #roster.append(Student("Matt"))
    #roster.append(Student("Mark"))
    #roster.append(Student("Chris"))
    #roster.append(Student("Isaac"))

    for count in range(10):
        name = input()
        grade = input()
        new_student = Student(name, grade)
        roster.append(new_student)
    

    #for count in roster:
        #grade = input()
        #roster.set_grade(grade)

    average_grade(roster)

    for student in roster:
        student.printStudentInfo(student)