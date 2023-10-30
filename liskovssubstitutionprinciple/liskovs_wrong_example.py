from abc import ABC, abstractmethod


class Member(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass

    @abstractmethod
    def pay(self):
        pass


class Teacher(Member):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print('saving teacher data to database')

    def pay(self):
        print('playing')


class Manager(Member):
    def __init__(self, name, age, manager_id):
        super().__init__(name, age)
        self.manager_id = manager_id

    def save_database(self):
        print('saving manager data to database')

    def pay(self):
        print('paying')


class Student(Member):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print('saving student data to database')

    def pay(self):
        raise NotImplementedError('it is free for student')


"""
Now this example cannot work! both classes are subclass of the member
class but the student class will throw exceptions or not work as expected.
this is against the rule. if a Member has to pay we can clearly say that a 
Student cannot be a member. to solve this problem we can remove the pay()
method from member and create a new abstract class payer.
"""


if __name__ == '__main__':
    members = [
        Teacher('vvv', 24, 12),
        Manager('vv', 44, 56),
        Student('vvvv', 24, 34)
    ]

    for member in members:
        member.pay()