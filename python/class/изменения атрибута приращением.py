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
        
    def increment_obometer(self, miles):
        self.obometer_reading += miles

my_used_car = car('subaru', 'outback', '2015',)
print(my_used_car.get_discriptive_name())

my_used_car.update_odometer (23_500)
my_used_car.read_obometer()

my_used_car.increment_obometer(100)
my_used_car.read_obometer()

