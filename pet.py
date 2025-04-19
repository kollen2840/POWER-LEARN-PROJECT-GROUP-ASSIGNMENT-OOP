#pet



class Pet:
  def __init__(self,name):
    self.name = name
    self.hunger = int(input(f"How Hungry is {self.name} upto 3  "))
    self.energy = int(input(f"How energetic is {self.name} upto 10  "))
    self.happiness = int(input(f"How happy is {self.name} upto 5  "))
    self.tricks = []
   
  def eat(self):
    self.hunger = max(0, self.hunger-3)
    self.happiness += 1
    
  def sleep(self):
    self.energy = min(10, self.energy + 5)
    
  def play(self):
    if self.energy >= 2:
      self.energy -= 2
      self.happiness += 2
      self.hunger += 1
      
    else:
      print(f"{self.name} is too tired")
      
  def train(self):
    trick1 = input(f"{self.name}'s Trick:  ")
    trick2 = input(f"{self.name}'s Trick:  ")
    trick3 = input(f"{self.name}'s Trick:  ")
    self.tricks.append(trick1)
    self.tricks.append(trick2)
    self.tricks.append(trick3)
 
  def show_tricks(self):
    print(f"{self.name} knows the following: {','.join(self.tricks)}")
  
  def get_status(self):
    print(f"NAME : {self.name} HUNGER: {self.hunger} ENERGY : {self.energy} HAPPINESS: {self.happiness} TRICKS {self.tricks}")