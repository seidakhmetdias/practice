class Employee:
    def init(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return float(self.base_salary)


class Manager(Employee):
    def init(self, name, base_salary, bonus_percent):
        super().init(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)


class Developer(Employee):
    def init(self, name, base_salary, completed_projects):
        super().init(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500


class Intern(Employee):
    pass


data = input().split()
role = data[0]

if role == "Manager":
    employee = Manager(data[1], int(data[2]), int(data[3]))
elif role == "Developer":
    employee = Developer(data[1], int(data[2]), int(data[3]))
elif role == "Intern":
    employee = Intern(data[1], int(data[2]))

print(f"Name: {employee.name}, Total: {employee.total_salary():.2f}")