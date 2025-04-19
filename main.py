#main

from pet import Pet

def main():
  my_pet = Pet(input("Your Pet Name   "))
  
  #print initual status
  
  my_pet.get_status()
  
  #status after
  
  my_pet.eat()
  my_pet.play()
  my_pet.sleep()
  
  
  my_pet.train()
  
  my_pet.show_tricks()
  
  my_pet.get_status()
  
if __name__ == "__main__":
  
  main()