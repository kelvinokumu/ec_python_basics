# abstract methods and classes

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine():
        pass
    
    def stop_engine():
        print("Stop Engine")

class Car(Vehicle):
    def start_engine():
        print("Starting the engine")

car = Car()
car.start_engine()



