#simple car class that includes accelerating and braking capabilities
class Car:
    def __init__(self, year_model, make):
        #initialize the car object with the given year_model and make
        self.__year_model = year_model
        self.__make = make
        #initialize the current speed to 0 
        self.__speed = 0
        #define the speed increment/decrement value
        self.__jump = 5 
    
    #
    def accelerate(self):
        #increase the car's speed by the value of __jump
        self.__speed += self.__jump
        
    #
    def brake(self):
        #decrease the cars speed by the value of __jump
        self.__speed -= self.__jump
        
    #
    def get_speed(self):
        #return the current speed of the car
        return self.__speed