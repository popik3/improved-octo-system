class car:

    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        self.obometer_reading = 0

    def get_discriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_obometer(self):
        print(f"This car has {self.obometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.obometer_reading:
            self.obometer_reading = mileage
        else:
            print("You can't roll back an obometer!")

my_new_car = car('audi', 'A4', '2019',)
print(my_new_car.get_discriptive_name())

my_new_car.update_odometer (23)
my_new_car.read_obometer()
