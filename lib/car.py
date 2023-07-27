from vehicle import Vehicle


class Car(Vehicle):

    # how to use the method from the Vehicle class from vehicle.py file

    # def gogo(self):
    #     Vehicle.go()
    
    def go():
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


car = Car(5, 4)
print(car.go())
