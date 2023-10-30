
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person name (name={self.name})'

    @staticmethod
    def save(person):
        print(f'save the {person} to database')


if __name__ == '__main__':
    person = Person('vinay')
    person.save(person)
