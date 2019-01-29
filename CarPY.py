
from termcolor import cprint
from termcolor import ATTRIBUTES

class Vehicle:

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_diff):
        self.speed += abs(speed_diff)
        self.speed = min(self.speed, self.max_speed)
        cprint(self.speed,'red')

    def decelerate(self, speed_diff):
        self.speed -= abs(speed_diff)
        self.speed = max(self.speed, -5)
        cprint(self.speed,'green')

class Car(Vehicle):
    pass
#Car class inherits properties from Vehicle class

class Bus(Vehicle):
    def decelerate(self, speed_diff):
        self.speed -= abs(speed_diff)
        self.speed = max(self.speed, 0)
        cprint(self.speed,'green')
"""    
    def decelerate(self, speed_diff):
        super().decelerate(speed_diff)
        self.speed = max(self.speed, 0)
        cprint(self.speed,'green')
"""        
#Bus class inherits properties from Vehicle class 
#BUT has exceptions (which are listed above) 
"""
In the Bus class, the slow_down method overrides the behavior of the parent class.
The super() statement makes a call to the parent class to find the new speed, and then makes
sure that this speed is not below 0 km/h.
"""
class Bike(Vehicle):
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = 30
        self.speed = 0
        '''
    def __init__(self, model, max_speed):
        max_speed = min(max_speed, 30)
        self.speed = max(self.speed, 0)
        self.speed = 0
        super().__init__(name, max_speed)
        '''


bmw_x6 = Car(model = "BMW X6", max_speed= 230)
print(bmw_x6.model)
bmw_x6.accelerate(250)
bmw_x6.decelerate(240)



bvannin = Bus(model= "Merc", max_speed= 100)
print(bvannin.model)
bvannin.accelerate(120)
bvannin.decelerate(200)


frogb = Bike(model="frog", max_speed= 40)
print(frogb.model)
frogb.accelerate(40)
frogb.decelerate(50)


#colored(bmw_x6.speed, 'red', 'on_grey', attrs=['blink'])