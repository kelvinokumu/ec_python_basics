class Car:
    
    # initialize
    def __init__(self, brand, color):
        self.car_brand = brand
        self.car_color = color

brand = input("Car Brand ")
color = input("Car Color ")

c = Car(brand, color)

print(c.car_brand)
print(c.car_color)