class vehicle: #parent class
    def __init__(self,name,maxspeed,mileage):
      self.name = name
      self.maxspeed = maxspeed
      self.mileage = mileage

class bus(vehicle): #child class inherited from parent class
   pass #empty but still it work ( not adding new details)

#object creation
v1 = bus("tesla", "i don't know", 55)
print("Tasheen's fav car is:",v1.name)

v2 = bus("BMW", "i don't know", 45)
print("Vedanshi's fav car is:",v2.name)