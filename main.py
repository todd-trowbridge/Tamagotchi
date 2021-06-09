from toy import Toy
from cuddlypet import CuddlyPet
from pet import Pet

pet_name = input("Name your pet: ")
pet_type = int(input("""
Which pet would you like?
1. Pet
2. Cuddly Pet
: """))

if pet_type == 1:
  pet = Pet(pet_name)
elif pet_type == 2:
  pet = CuddlyPet(pet_name)

while True:
  print(pet)
  print("""
1. Feed Pet
2. Play with Pet
3. Do Nothing
4. Give Toy""")
  choice = int(input(': '))
  if choice == 1:
    # feed the pet
    pet.eat_food()
  elif choice == 2:
    # play with pet
    pet.get_love()
  elif choice == 4:
    pet.give_toy(Toy())
  pet.be_alive()
  if not pet.is_alive():
    print(pet.get_status())
    print(f"RIP {pet.name}")
    break
  
  # each time the loop runs, reduce the pet stats
  pet.be_alive()