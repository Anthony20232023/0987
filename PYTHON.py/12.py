class Vehicle:
    def move(self):
        print("This vehicle moves... somehow.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚢")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
