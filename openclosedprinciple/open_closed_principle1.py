from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Tester(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print('Tester is testing..')


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print('Developer is developing..')


class Company:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def work(employee):
        employee.work()


if __name__ == '__main__':
    company = Company('motorola')
    developer = Developer('vinay', 28)
    tester = Tester('akshay', 2)
    company.work(developer)
    company.work(tester)

