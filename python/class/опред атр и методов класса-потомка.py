class car():
    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year

    def get_descroptive_name (self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class electric_car(car):

    def __init__ (self,make,model,year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля"""
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print (f"This car has a {self.battery_size}-kWh battery")

my_tesla = electric_car('tesla', 'model s', 2019)
print(my_tesla.get_descroptive_name())
my_tesla.describe_battery()