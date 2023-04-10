from abc import ABC, abstractmethod

"""
if S is a subtype of T, 
then objects of type T may be replaced by objects of type S, 
without breaking the program.
"""


class Member(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass


class Teacher(Member):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print('saving teacher data to database')


class Student(Member):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print('saving student data to database')


if __name__ == '__main__':
    members = [
        Student('vinay', 24, 12345),
        Teacher('amar', 50, '6789')
    ]

    for member in members:
        member.save_database()
