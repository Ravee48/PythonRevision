class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, first_name):
        new_name = first_name + " " +self.name.split()[1]
        self.name = new_name
        # return new_name




e = Employee("Ravi Kumar", 90)
print(e.name)
# print(e.first_name())
# print(e.new_first_name("Mohini"))


e.first_name = "John"
print(e.name)