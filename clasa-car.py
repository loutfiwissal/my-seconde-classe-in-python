class car () :
    def __init__(self,name, color, model, speed, nitrospeed, enginepower):
        self.name=name
        self.color=color
        self.model=model
        self.speed=speed
        self.nitrospeed=nitrospeed
        self.enginepower=enginepower

    def car(self):
        print("the car name {} his color {} his model {} his speed {} KM/H nitrospeed {} enginepower {} PS"
              .format(self.name, self.color, self.model, self.speed, self.nitrospeed, self.enginepower))
        
car1 = car("Mercedes", "black", "S63 AMG COUPE", 314, 100, 802)

car1.car()