class Vehicles():
    def start_engine(self):
        res = "engine started"
        return res
    
    
    def stop_engine(self):
        pass


class Car(Vehicles):
    pass


car = Car()
print(car.start_engine())
