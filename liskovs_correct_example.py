from abc import ABC, abstractmethod


class Payer(ABC):
    @abstractmethod
    def pay(self):
        pass


class Member(ABC):
    @abstractmethod
    def save_database(self):
        pass


class Teacher(Member, Payer):
    def __init__(self, name, age, teacher_id):
        self.name = name
        self.age = age
        self.teacher_id = teacher_id

    def save_database(self):
        print('saving teacher data to database')

    def pay(self):
        print('teacher playing')


class Manger(Member, Payer):
    def __init__(self, name, age, manager_id):
        self.manager_id = manager_id

    def save_database(self):
        print('saving manager data to database')

    def pay(self):
        print('manager paying')


class Student(Member):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def save_database(self):
        print('saving student data to database')


if __name__ == '__main__':
    payers = [
        Teacher('john', 30, '123'),
        Manger('Mary', 24, '456')
    ]

    for payer in payers:
        payer.pay()
