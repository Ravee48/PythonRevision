class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        info = f"The company name is : {self.company}, Employee name is : {self.name}, with salary : {self.salary}"
        print(info)

    # Static method
    @staticmethod
    def sum(a, b):
        return a + b

    # Class Method
    @classmethod
    def change_company_name(self, new_name):
        self.company = new_name

e = Employee("Ravi", 12000)
e.print_info()
print(e.sum(43, 35))

print(e.company)
e.change_company_name("Paytm")
print(e.company)