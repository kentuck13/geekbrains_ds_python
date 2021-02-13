class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


employee = Position('Alexander', 'A', 'DS', {'wage': 100, 'bonus': 100})
print(employee.get_full_name())
print(employee.get_total_income())
