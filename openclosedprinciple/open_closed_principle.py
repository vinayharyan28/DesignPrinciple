""" A class must be open to extension but closed to modification.
    When we want to add new things to our model, we only want to add new things &
    not change anything existing that is closed to modification.
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Tester(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def test(self):
        print(f'{self.name} is testing')


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def develop(self):
        print(f'{self.name} is developing')


class Company:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def work(employee):
        if isinstance(employee, Developer):
            employee.develop()
        elif isinstance(employee, Tester):
            employee.test()
        else:
            raise Exception('unknown employee')


if __name__ == '__main__':
    tester = Tester('Akshay', 5000)
    developer = Developer('Vinay', 5000)
    company = Company('TATA')
    company.work(tester)
    company.work(developer)



