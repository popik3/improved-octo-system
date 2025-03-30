class Employee():
    def __init__(self, name, first_name, annual_salary, give_raise):
        self.first_name = first_name
        self.name = name
        self.annul_salary = annual_salary + give_raise
    
    def information_of_worker(self):
        print(f"{self.first_name} {self.name} {self.annul_salary}")
    
    def get(self):
        self.give_raise.append()

